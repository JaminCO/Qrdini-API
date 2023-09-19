import requests

import json 

url = "http://127.0.0.1:8080/"

def generate():
    r = requests.get(url+"generate?data=TESTING")
    print(r)
    print(r.json())
    return r.json()["data"]["url"]

def delete(file_url):
    payload = {"file_url":file_url}
    r = requests.delete(url+"/delete/", data=json.dumps(payload))
    print(r)
    print(r.json())
    return r.json()

url = generate()
print(url)
delete(url)
print("ALL TEST PASSED")

















"""
PYMONGO
"""

# import pymongo
# import json

# # Connect to MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["QRAPI"]
# collection = db["Qrcode"]


# # Create index for efficient retrieval
# # collection.create_index("name")

# code = {"name":"Test image", "file_url":"<url>"}

# # Add courses to collection
# x = collection.insert_one(code)
# print(x.inserted_id)
# # Close MongoDB connection
# client.close()