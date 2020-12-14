from pymongo import MongoClient

client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=2)
db = client["learn_api"]
users_collection = db["users"]


def check_mongo_connection():
    if client.server_info():
        return print("Mongo is connected on {}".format(client))
    else:
        return print("not connected"), exit()


def insert_user(name: str):
    try:
        document = {
            "name": name
        }
        inserted_name = users_collection.insert_one(document)

        return print("The name: '{}' was added in mongo with id: {}".format(name, inserted_name.inserted_id))

    except Exception as e:
        return e


def insert_details_in_db(details: dict):
    try:
        inserted_details = users_collection.insert_one(details)
        return "The details: '{}' were added in mongo with id: {}".format(name, inserted_details.inserted_id)
    except Exception as e:
        return e


def clear_collection(collection: str):
    try:
        cleared_collection = db[collection].drop()
        return print("'{}' collection dropped".format(collection))

    except Exception as e:
        return e
