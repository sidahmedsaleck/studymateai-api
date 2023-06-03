from flask import Flask
from flask_restful import Api, Resource
from .config import config_by_name


class Home(Resource):
    
    def get(self):
        return {
        "msg":"welcome to studyMate"
        }


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    api = Api(app)


    api.add_resource(Home,'/')
    
    return app