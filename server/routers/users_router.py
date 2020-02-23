from flask import Blueprint,request,jsonify, make_response
from ..config import db
from ..db import users_db
from flask_cors import cross_origin
import json





users_list = db['users']

users = Blueprint('users', __name__)
@users.route("/register", methods=['POST'])
@cross_origin(supports_credentials=True)
def register():
    users_details = request.get_json()
    result = users_db.add_user(users_details)
    if result:
        user = result
        return create_cookie(user)


@users.route("/register", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_users():
    return jsonify(users_db.get_users())


# not working   cors origin problem
@users.route("/login", methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def login():
    users_details = request.get_json()
    response = users_db.login(users_details)
    if response:
        details = response
        create_cookie(details)
    return jsonify({"user": details})


def create_cookie(details):
    res = make_response("Setting a cookie")
    print(str(details))
    res.set_cookie('auth', details, max_age=60 * 60 * 24 * 365 * 2)
    return res

