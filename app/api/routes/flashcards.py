from flask_restful import Resource

class TextFlashcards(Resource):

    def get(self):
        return dict(
            msg="Text Flashcards route"
        )
    


class PdfFlashcards(Resource):

    def get(self):
        return dict(
            msg="Pdf Flashcards route"
        )
