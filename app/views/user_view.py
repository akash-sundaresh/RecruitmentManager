"""
Author      : Akash Sundaresh
Date        : 08-12-2019
Description : User view code
"""

from flask.views import MethodView
from flask import request
import json

from app.models.user_model import User


class UserView(MethodView):
    methods = ['GET', 'POST', 'PUT', 'DELETE']

    def get(self, user_email=None):
        if not user_email:
            return User.objects.to_json()
        else:
            user = User.objects(user_email=user_email)
            if user:
                return user.to_json()
        return "Record Not found", 404

    def post(self):
        data = json.loads(request.data)
        new_user = User()
        new_user.username = data['username']
        new_user.user_email = data['user_email']
        new_user.location = data.get('location')
        _id = new_user.save()
        return str(_id.id), 201

    def put(self, user_email=None):
        data = json.loads(request.data)
        if user_email:
            user = User.objects(user_email=user_email)
            if user:
                if 'user_email' in data.keys():
                    del data['user_email']
                if user.update(**data):
                    return "Success", 200
                return "Failed to update", 500
            return "Invalid user_email", 404
        return "Method not allowed", 405

    def delete(self, user_email=None):
        if user_email:
            user = User.objects(user_email=user_email)
            if user:
                user.delete()
                return "Success", 200
            return "Invalid user_email", 404
        return "Method not allowed", 405
