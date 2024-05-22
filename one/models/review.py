#!/usr/bin/python3
"""
This Defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This Represent a review.

    Attributes:
        user_id (str): The id of the user
        place_id (str): The Place id.
        text (str): text of the review.
    """

    user_id = ""
    place_id = ""
