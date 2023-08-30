# Import Modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import qrcode
import random
from pydantic import BaseModel
from typing import Optional
import requests
from dotenv import load_dotenv
import os
import pymongo
import json

# Connect to MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["QRAPI"]
# collection = db["Qrcode"]

# Create server
app = FastAPI()
load_dotenv()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)


# Delete the image from the cloud
def delete_file(file_url):
    url = "https://api.uploadfly.cloud/delete"

    headers = {
      "Authorization": os.getenv("API_KEY_ALL"),
    }
    body = {
      'file_url': file_url,
    }
    r = requests.delete(url, headers=headers, json=body)
    return r

# Store in cloud and get link
def upload_file(filename):
    url = "https://api.uploadfly.cloud/upload"

    headers = {
      'Authorization':  os.getenv("API_KEY_UPLOAD"),
    }
    body = {
      'file': open(filename, 'rb'),
    }
    r = requests.post(url, headers=headers, files=body)
    return r

@app.get("/")
async def home():
    return {"message": "Hello World"}

# Generate name:
def gen_name():
    name = "QRAPI-"+str(random.randint(1172, 9728))+"Codeimg"
    return name

# Create a Pydantic model
class Qrcode(BaseModel):
    # name: str
    data: str = "QRCODE MESSAGE"


class DELCODE(BaseModel):
    # name: str
    file_url: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "file_url":"<pass-url-here>"
            }
        }


# Create QRcodes
def create(name, data):
    qr = qrcode.QRCode(
            version = 15,
            box_size = 10,
            border = 5
        )

    data_info = data

    qr.add_data(data_info)
    qr.make(fit = True)
    img = qr.make_image(fill="black",back_color = "white")
    image_name = name
    img.save(image_name + '.png')

# Get message/url and generate code
@app.post("/generate/")
async def generate(qrcode: Qrcode):
    msg = qrcode.data
    name = gen_name()
    create(name, msg)
    res = upload_file(name+".png")
    
    # code = {"name":res.json()["data"]["name"], "file_url":res.json()["data"]["url"]}
    # # Add courses to collection
    # x = collection.insert_one(code)
    # print(x.inserted_id)
    # # Close MongoDB connection
    # client.close()

    return res.json()

@app.delete("/delete/")
async def delete(delcode: DELCODE):
    res = delete_file(delcode.file_url)
    return res.json()


# Store in cloud and get link
""" 
Upload CODE IMG in cloud platform
return link/specs

{
    'success': True,
    'status': 201, 
    'data': {
        'url': 'https://cdn.uploadfly.cloud/fhRp8N/QRAPI-2001Codeimg.png',
        'path': 'fhRp8N/QRAPI-2001Codeimg.png',
        'type': 'text/plain', 
        'size': '2.42 kB', 
        'name': 'QRAPI-2001Codeimg.png'
}
}
"""

# main
"""
"""

# Run server
