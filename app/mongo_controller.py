from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["learn_api"]
users_collection = db["users"]

def insert_user(name: str):
    try:
        document = { 
            "name": name
        }
        inserted_name = users_collection.insert_one(document)

        return print("The name: '{}' was added in mongo with id: {}".format(name,inserted_name.inserted_id))
        
    except Exception as e:
        return e

def clear_collection(collection: str):
    try:
        cleared_collection = db[collection].drop()
        return print("'{}' collection dropped".format(collection))
    
    except Exception as e:
        return e


