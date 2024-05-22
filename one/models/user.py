#!/usr/bin/python3
"""
This Defines the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        first_name (str): The user first name
        last_name (str): The user last name
        email (str): The email of the user.
        password (str): The password of the user.
    """

    first_name = ""
    last_name = ""
    email = ""
