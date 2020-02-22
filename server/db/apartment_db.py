from ..db import query_builder
from ..config import db

apartments = db["apartments"]


def get_recent_apartment():
    apartments_result = []
    for apartment in apartments.find({}, {"_id": 0}).limit(4):
        apartments_result.append(apartment)
    return apartments_result


def get_apartments_by_id(apartment_id):
    return apartments.find_one({"id": int(apartment_id)}, {"_id": 0})


def get_all_apartments(query):
    apartments_result = []
    for apartment in apartments.find(query_builder.apartment_filters(query), {"_id": 0}):
        apartments_result.append(apartment)
    return {'apartments': apartments_result}


def get_country_apartments():
    countries = []
    for apa in apartments.aggregate([ {"$group" : {'_id':"$country"}}]):
        countries.append(apa["_id"])
        print(countries)
