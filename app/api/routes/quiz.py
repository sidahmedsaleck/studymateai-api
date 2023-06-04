import io
from flask import request
from flask_restful import Resource
from app.api.controller.quiz import pdfQuizController, textQuizController
from app.api.middlewares.verifyAuth import verifyAuth

class TextQuiz(Resource):

    def get(self):
    
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
        res = textQuizController(text,tire,lang)

        if res:
            return res
        else:
            return {
                "success":False,
                "msg":"err in routes/quiz.py/textquiz"
            }
    
class PdfQuiz(Resource):

    def get(self):
        
        #args parssing
        print("args")
        args = request.form
        authId = args['authId']
        fileName = args['fileName']
        tire = args['tire']
        lang = args['lang']
        fileBytes = request.files[fileName].stream.read()
        print("fileBytes")
        fileBytes = io.BytesIO(fileBytes)


        # verifying the authId
        if not verifyAuth(authId):
            return {'success':False,
                    'message':'auth token is not valid'},401
            

        res = pdfQuizController(fileBytes,tire,lang)
        
        if res:
            return res
        else:
            return {
                "success":False,
                "msg":"err in routes/quiz.py/pdfquiz"
            }
