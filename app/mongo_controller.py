from pymongo import MongoClient
import json
from dotenv import load_dotenv
load_dotenv()


client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=2)
db = client["learn_api"]
users_collection = db["users"]


def check_mongo_connection():
    if client.server_info():
        return True
    else:
        return False


def insert_details_in_db(details):
    try:
        print(details)
        users_collection.insert(dict(details))
        # users_collection.insert_one(details)
        return True
    except Exception as e:
        return e


def clear_collection(collection: str):
    try:
        cleared_collection = db[collection].drop()
        return print("'{}' collection dropped".format(collection))

    except Exception as e:
        return e

def get_details_from_collection(username: str):

    fetched_details = users_collection.find_one({"username": username}, {'_id': 0})  ####{'_id': 0} Excludes ObjectId
    if fetched_details == None:
        fetched_details = "Username does not exist"
    return fetched_details
    
def delete_details_from_collection(username: str):
    try:
        counter = users_collection.find({"username": username}).count()
        print(counter)
        if counter > 0:
            deleted_details = users_collection.remove({"username": username})
            response = {username: "Removed!"}
        else:
            response = {"Username does not exists!"}
        return response
    except Exception as e:
        return e