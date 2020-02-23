import uuid
from passlib.hash import pbkdf2_sha512
from ..config import db

users = db['users']


def add_user(users_details):
    hash_password = pbkdf2_sha512.using(rounds=10000, salt_size=64,).hash(str(users_details["password"]))
    users_details["password"] = hash_password
    users_details["_id"] = uuid.uuid1()  # got problem to get random id from mongodb
    users_details["status"] = "active"
    if not users_details["role_id"]:
        users_details["role_id"] = 2
    if users.insert_one(users_details).inserted_id:
        return users_details


def get_users():
    users_list = []
    for user in users.find({}, {"_id": 0}):
        users_list.append(user["email"])
    return users_list


def login(user_details):
    user = users.find_one({"email": user_details["user"]}, {"_id": 0})
    if user and pbkdf2_sha512.verify(user_details["password"], user["password"]):
        return user
    return False




