"""
Author      : Akash Sundaresh
Date        : 07-12-2019
Description : Model definition for Room collection
"""
from mongoengine import *


class Room(DynamicDocument):
    name = StringField(required=True)
    email = EmailField(required=True)
    location = StringField()
