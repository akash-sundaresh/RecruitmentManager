"""
Author      : Akash Sundaresh
Date        : 07-12-2019
Description : Model definition for User collection
"""

from mongoengine import *


class User(DynamicDocument):
    username = StringField(required=True, max_length=100)
    user_email = EmailField(required=True)
    location = StringField()
