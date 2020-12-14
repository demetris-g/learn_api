from flask import Flask, request as flask_request
from requests import request
from time import sleep
from app.mongo_controller import insert_user, clear_collection, insert_details_in_db, check_mongo_connection
from pprint import pprint
from app.validate import validate_details

app = Flask(__name__)


@app.route('/')
def documentation():
    return "here you will find nothing! Sorry :)\n"


@app.route('/name/<name>')
def hello(name: str):
    try:
        insert_user(name)
        return "Hello {}!\n Adding the name in the database!".format(name)

    except Exception as e:
        return e


@app.route('/empty/<collection>')
def empty_collection(collection: str):
    try:
        clear_collection(collection)
        return "Collection '{}' is empty now!".format(collection)
    except Exception as e:
        return e


@app.route('/insert/details', methods=['POST'])
def post_json():
    try:
        print(flask_request.is_json)
        content = dict(flask_request.get_json())
        pprint(content)
        if validate_details(content):
            insert_details_in_db(content)
            return 'Thank you for submitting your details'
        else:
            return 'Not valid details!'
    except Exception as e:
        return e


if __name__ == '__main__':
    check_mongo_connection()
    app.run(host='0.0.0.0', port="1453")
