from flask import jsonify, request, Blueprint
from flask_cors import cross_origin
from ..db import apartment_db

mod = Blueprint('mod', __name__)


@mod.route("/apartments", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_apartments():
    query = request.args
    apartments = apartment_db.get_all_apartments(query)
    return jsonify(apartments)


@mod.route('/apartments/four/bydate', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_recent_apartment():
    apartments = apartment_db.get_recent_apartment()
    return jsonify(apartments)


@mod.route('/apartments/<string:apartment_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_apartments_by_id(apartment_id):
    apartment = apartment_db.get_apartments_by_id(apartment_id)
    return jsonify([apartment])


@mod.route('/apartments/all/countries', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_country():
    apartment = apartment_db.get_country_apartments()
    return jsonify(apartment)


