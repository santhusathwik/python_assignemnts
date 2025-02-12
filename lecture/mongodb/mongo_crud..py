from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create or connect to a database
db = client["myDatabase"]

# Create or connect to a collection (table equivalent in RDBMS)
collection = db["users"]

print("Connected to MongoDB!")


collection.delete_many({"age": {"$lt": 30}})