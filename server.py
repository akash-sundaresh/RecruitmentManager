"""
Author      : Akash Sundaresh
Date        : 28-11-2019
Description : Main file which starts the web server. All pre-requisites will
be setup here.
"""
# library imports
from flask import Flask
from mongoengine import connect
# User imports
from app.config import *


app = Flask(__name__)
from app.urls import *


def _setup_database():
    connect("manager", host=MONGO_HOST, port=MONGO_PORT)


if __name__ == '__main__':
    _setup_database()
    app.run(debug=DEBUG)
