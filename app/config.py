"""
Author      : Akash Sundaresh
Date        : 07-12-2019
Description : All Application level config variables to be contained here
"""

MONGO_HOST = 'localhost'
MONGO_PORT = 27017


TEST_ENV = True
if TEST_ENV:
    DEBUG = True
