from flask_restful import Resource

class TextQuiz(Resource):

    def get(self):
        return dict(
            msg="TextQuiz route"
        )
    
class PdfQuiz(Resource):

    def get(self):
        return dict(
            msg="PdfQuiz route"
        )

