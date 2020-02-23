import os
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://EylonKoenig:a6310259@cluster0-arujk.gcp.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
db = cluster["realtor"]

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'lucyintheskywithdiamonds')
    PASSWORD_HASH = os.environ.get('PASSWORD_HASH', 'pbkdf2:sha256:50000$nbDXyw4q$d63296ea4de3e6954036cb2b8b87cd488be31a36d56795f62076dafdebe7cb3c')
    TOKEN_EXPIRATION = int(os.environ.get('TOKEN_EXPIRATION', 3600))
    MONGO_URI = "mongodb+srv://EylonKoenig:a6310259@cluster0-arujk.gcp.mongodb.net/test"
