
import pymongo
import json

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["QRAPI"]
collection = db["Qrcode"]


# Create index for efficient retrieval
# collection.create_index("name")

code = {"name":"Test image", "file_url":"<url>"}

# Add courses to collection
x = collection.insert_one(code)
print(x.inserted_id)
# Close MongoDB connection
client.close()