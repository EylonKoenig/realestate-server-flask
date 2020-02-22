from flask import Blueprint,request,jsonify, make_response
from ..config import db
from ..db import users_db

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper



def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
                attach_to_all=True, automatic_options=True):
    """Decorator function that allows crossdomain requests.
      Courtesy of
      https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
    """
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    # use str instead of basestring if using Python 3.x
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    # use str instead of basestring if using Python 3.x
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        """ Determines which methods are allowed
        """
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        """The decorator function
        """
        def wrapped_function(*args, **kwargs):
            """Caries out the actual cross domain code
            """
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


users_list = db['users']

users = Blueprint('users', __name__)
@users.route("/register", methods=['POST'])
def register():
    users_details = request.get_json()
    result = users_db.add_user(users_details)
    if result:
        user = result
        return create_cookie(user)


@users.route("/register", methods=['GET'])
def get_users():
    return users_db.get_users()


# not working   cors origin problem
@users.route("/login", methods=['POST', 'OPTIONS'])
def login():
    users_details = request.get_json()
    response = users_db.login(users_details)
    if response:
        details = response
        create_cookie(details)
    return jsonify({"result": True})


def create_cookie(details):
    res = make_response("Setting a cookie")
    res.set_cookie('auth', details, max_age=60 * 60 * 24 * 365 * 2)
    return res

