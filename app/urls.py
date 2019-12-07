"""
Author      : Akash Sundaresh
Date        : 08-12-2019
Description : 
"""

from server import app
from .views.user_view import UserView
from .views.room_view import RoomView


# Defining the view once, as multiple urls can point to same view.
user_view = UserView.as_view('user_api')
room_view = RoomView.as_view('room_api')


# Declare all URLs after the views are defined
app.add_url_rule('/users', view_func=user_view)
app.add_url_rule('/users/<user_email>', view_func=user_view)

app.add_url_rule('/rooms', view_func=room_view)
app.add_url_rule('/rooms/<email>', view_func=room_view)


