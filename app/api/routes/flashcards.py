import io
from flask import request
from flask_restful import Resource
from app.api.controller.flashcards import pdfFlashcardsController, textFlashcardsController

from app.api.middlewares.verifyAuth import verifyAuth

class TextFlashcards(Resource):

    def post(self):

        #args parssing
        args = request.form
        authId = args['authId']
        text = args['text']
        tire = args['tire']
        lang = args['lang']

        # verifying the authId
        if not verifyAuth(authId):
            return {'success':False,
                    'message':'auth token is not valid'},401
        
        # calling the controller
        res = textFlashcardsController(text,tire,lang)

        if res:
            return res
        else:
            return {
                "success":False,
                "msg":"err in routes/flashcards.py/textFlashcards"
            }
    


class PdfFlashcards(Resource):

    def post(self):
        
        #args parssing
        args = request.form
        authId = args['authId']
        fileName = args['fileName']
        tire = args['tire']
        lang = args['lang']
        fileBytes = request.files[fileName].stream.read()
        fileBytes = io.BytesIO(fileBytes)


        # verifying the authId
        if not verifyAuth(authId):
            return {'success':False,
                    'message':'auth token is not valid'},401
        
        res = pdfFlashcardsController(fileBytes,tire,lang)

        if res:
            return res
        else:
            return {
                "success":False,
                "msg":"err in routes/flashcards.py/pdfFlashcards"
            }
        



