from flask import Flask
from requests import request
from time import sleep
from app.mongo_controller import insert_user, clear_collection

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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port="1453")