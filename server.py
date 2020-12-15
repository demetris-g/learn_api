from app.mongo_controller import clear_collection, insert_details_in_db, check_mongo_connection, get_details_from_collection, delete_details_from_collection
from pprint import pprint
from app.validate import validate_details, UserDetails
from fastapi import FastAPI

#FastApi
app = FastAPI()


@app.get('/')
def check_db_connection():
    try:
        check_mongo_connection()
        return {"Connected"}
    except:
        return {"Check database connection"}

@app.delete('/collection/delete')
def empty_collection(collection: str):
    try:
        clear_collection(collection)
        return "Collection '{}' is empty now!".format(collection)
    except Exception as e:
        return e

@app.post('/details/insert')
def post_details(details: UserDetails):
    try:
        print(details)
        insert_details_in_db(details)
        return {'Thank you for submitting your details'}
    except Exception as e:
        return e

@app.get('/details/get')
def get_details(username: str):
    try:
        response =  get_details_from_collection(username)
        pprint(response)
        return response
    except Exception as e:
        return e

@app.delete('/details/delete')
def delete_details(username: str):
    try:
        response =  delete_details_from_collection(username)
        pprint(response)
        return response
    except Exception as e:
        return e
