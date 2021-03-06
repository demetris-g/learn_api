import json
from pydantic import BaseModel, ValidationError, validator
from re import match
from .mongo_controller import users_collection
from typing import Optional

class UserDetails(BaseModel):
    full_name: str
    username: str
    email: Optional[str] = None  
    telno: Optional[str] = None
    password: str
    confirm_password: str

    @validator('full_name')
    def validate_fullname(cls, valid_name):
        if not match('[A-Za-z]{2,25}\s[A-Za-z]{2,25}', valid_name):
            raise ValueError(
                'Fullname must contain a space between first name and last name')
        return valid_name.title()

    @validator('username')
    def validate_username(cls, valid_username):
        if ' ' in valid_username or len(valid_username) not in range(6, 30):
            raise ValueError(
                'Try another username!\n  Must be 6-30 characters and do not include space')

        duplicate_name = users_collection.find(
            {"username": valid_username}).count()
        if duplicate_name > 0:
            raise ValueError("Username already exists!")

        return valid_username
    
    @validator('email')
    def validate_email(cls, valid_email):
        if not match('^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', valid_email):
            raise ValueError("Not a valid email address")
        return valid_email

    @validator('password')
    def validate_password(cls, valid_password):
        if ' ' in valid_password or len(valid_password) not in range(8, 30):
            raise ValueError(
                'Try another password!\n  Must be 8-30 characters and do not include space')
        return valid_password

    @validator('confirm_password')
    def validate_matching_passwords(cls, valid_match, values,  **kwargs):
        if 'password' in values and valid_match != values['password']:
            raise ValueError('Passwords do not match!')
        return valid_match


def validate_details(details: dict):
    try:
        UserDetails(
            full_name=details['full_name'],
            username=details['username'],
            password=details['password'],
            confirm_password=details['confirm_password']
        )
        return True
    except ValidationError as e:
        print(e)
        return False


# TEST validation
# body = {
#     'full_name': "Dimitris Georgiou",
#     'username': "dasdsada",
#     'password': '12345678',
#     'confirm_password': '12345678'
# }


# validate_details(body)
