from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_mongoengine import MongoEngine
from server.config import Config


def create_app(config_class=Config):
    from server.routers.apartments_router import mod
    from server.utils import utils
    app = Flask(__name__)
    CORS(app, support_credentials=True)
    app.config.from_object(Config)
    app.register_blueprint(mod)
    app.register_blueprint(utils)
    app.run(host='localhost', port=4000, debug=True)
    app.logger.info("Server shutting down")
    auth = HTTPBasicAuth()
    mongo = MongoEngine(app)

    return app

