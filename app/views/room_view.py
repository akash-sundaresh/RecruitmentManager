"""
Author      : Akash Sundaresh
Date        : 08-12-2019
Description : 
"""

from flask.views import MethodView
from flask import request
import json

from app.models.room_model import Room


class RoomView(MethodView):
    methods = ['GET', 'POST', 'PUT', 'DELETE']

    def get(self, email=None):
        if not email:
            return Room.objects.to_json()
        else:
            room = Room.objects(email=email)
            if room:
                return room.to_json()
        return "Record Not found", 404

    def post(self):
        data = json.loads(request.data)
        new_room = Room()
        new_room.name = data['name']
        new_room.email = data['email']
        new_room.location = data.get('location')
        _id = new_room.save()
        return str(_id.id), 201

    def put(self, email=None):
        data = json.loads(request.data)
        if email:
            room = Room.objects(email=email)
            if room:
                if 'email' in data.keys():
                    del data['email']
                if room.update(**data):
                    return "Success", 200
                return "Failed to update", 500
            return "Invalid email", 404
        return "Method not allowed", 405

    def delete(self, email=None):
        if email:
            room = Room.objects(email=email)
            if room:
                room.delete()
                return "Success", 200
            return "Invalid email", 404
        return "Method not allowed", 405
