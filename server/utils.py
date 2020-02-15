import os
import uuid
from flask import jsonify, send_file, abort, Blueprint

utils = Blueprint('utils', __name__)

def generate_id():
    return str(uuid.uuid4())


def validate_path(path):
    if not os.path.exists(path):
        abort(404)


@utils.errorhandler(404)
def not_found(error):
    return jsonify(error='not found'), 404


@utils.errorhandler(400)
def bad_request(error):
    return jsonify(error='bad request'), 400


@utils.errorhandler(405)
def not_allowed(error):
    return jsonify(error='method not allowed'), 405


@utils.route('/api/3/ping', methods=['GET'])
def ping():
    return jsonify(result=True)


@utils.route('/images/<string:path>/<string:image_name>')
def get_image(path, image_name):
    image = "public/images/"+path+"/"+image_name
    return send_file(image)

