
import io
from flask_restful import Resource
from flask import request
from app.api.middlewares.verifyAuth import verifyAuth 
from app.api.controller.summary import pdfSummaryController, textSummaryController



class TextSummary(Resource):

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
            
        res = textSummaryController(text,tire,lang)
        
        if res:
            return res
        else:
            return {
                "success":False,
                "msg":"err in routes/summary.py/textSummary"
            }



class PdfSummary(Resource):
    
    def get(self):

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
            

        res = pdfSummaryController(fileBytes,tire,lang)
        
        if res:
            return res
        else:
            return {
                "success":False,
                "msg":"err in routes/summary.py/pdfSummary"
            }
        
    