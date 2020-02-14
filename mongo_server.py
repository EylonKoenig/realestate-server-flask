import os
import uuid
import apartment_db
from flask import Flask, jsonify, send_file, abort, request
from flask_cors import CORS, cross_origin
from flask_httpauth import HTTPBasicAuth
from flask_mongoengine import MongoEngine


SECRET_KEY = os.environ.get('SECRET_KEY', 'lucyintheskywithdiamonds')
PASSWORD_HASH = os.environ.get('PASSWORD_HASH', 'pbkdf2:sha256:50000$nbDXyw4q$d63296ea4de3e6954036cb2b8b87cd488be31a36d56795f62076dafdebe7cb3c')
TOKEN_EXPIRATION = int(os.environ.get('TOKEN_EXPIRATION', 3600))
MONGO_URI = "mongodb+srv://EylonKoenig:a6310259@cluster0-arujk.gcp.mongodb.net/test"

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config.from_object(__name__)
auth = HTTPBasicAuth()
mongo = MongoEngine(app)


def generate_id():
    return str(uuid.uuid4())


def validate_path(path):
    if not os.path.exists(path):
        abort(404)



@app.errorhandler(404)
def not_found(error):
    return jsonify(error='not found'), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify(error='bad request'), 400


@app.errorhandler(405)
def not_allowed(error):
    return jsonify(error='method not allowed'), 405


@app.route('/api/3/ping', methods=['GET'])
def ping():
    return jsonify(result=True)


@app.route('/images/<string:path>/<string:image_name>')
def get_image(path, image_name):
    image = "images/"+path+"/"+image_name
    validate_path(image)
    return send_file(image)


@app.route('/apartments/four/bydate', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_recent_apartment():
    apartments = apartment_db.get_recent_apartment()
    return jsonify(apartments)


@app.route('/apartments', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_apartments():
    query = request.args
    print(query)
    # apartments = apartment_db.get_all_apartments(query)
    # return jsonify(apartments)
    return jsonify(result=True)


@app.route('/apartments/<string:apartment_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_apartments_by_id(apartment_id):
    apartment = apartment_db.get_apartments_by_id(apartment_id)
    return jsonify([apartment])


if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
    app.logger.info("Server shutting down")


