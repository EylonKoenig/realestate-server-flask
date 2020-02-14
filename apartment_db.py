from pymongo import MongoClient
import query_builder

cluster = MongoClient("mongodb+srv://EylonKoenig:a6310259@cluster0-arujk.gcp.mongodb.net/test")
db = cluster["realtor"]
apartments = db["apartments"]


def get_recent_apartment():
    apartments_result = []
    for apartment in apartments.find({}, {"_id": 0}).limit(4):
        apartments_result.append(apartment)
    return apartments_result


def get_apartments_by_id(apartment_id):
    return apartments.find_one({"id":int(apartment_id)},{"_id":0})


def get_all_apartments(query):
    apartments_result = []
    for apartment in apartments.find(query_builder.apartment_filters(query), {"_id": 0}).limit(4):
        apartments_result.append(apartment)
    return apartments_result


