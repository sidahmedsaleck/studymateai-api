from flask import Flask
from flask_restful import Api, Resource
from .config import config_by_name
from .routes.summary import TextSummary, PdfSummary
from .routes.quiz import TextQuiz, PdfQuiz
from .routes.flashcards import PdfFlashcards, TextFlashcards


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
    
    api.add_resource(TextSummary,'/api/summary/text')
    api.add_resource(PdfSummary,'/api/summary/pdf')
    
    api.add_resource(TextQuiz,'/api/quiz/text')
    api.add_resource(PdfQuiz,'/api/quiz/text')

    api.add_resource(TextFlashcards,'/api/flashcards/text')
    api.add_resource(PdfFlashcards,'/api/flashcards/text')
    
    return app