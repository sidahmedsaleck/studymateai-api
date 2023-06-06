
from app.api.utils import FREE_TIRE_CHARACTERS_LIMIT , PAIED_TIRE_CHARACTERS_LIMIT
from app.api.service.pdf import PdfService
from app.api.service.summary import SummaryService

def pdfSummaryController(file,tire:str,lang:str):
    
    try:

        # getting the number of charcter to use
        charctersLimit = FREE_TIRE_CHARACTERS_LIMIT if tire.lower()=='free' else PAIED_TIRE_CHARACTERS_LIMIT
        
        #extracting plain text from the file
        plainText = PdfService(file,charctersLimit).getText()

        # creating the summaries
        summary, totalTokenUsed, totalCost = SummaryService(plainText,lang).getLangChainSummary()

        # returning the summaries to the user
        if summary:
                
            return {'success': True,
                    'totalTokensUsed':totalTokenUsed,
                    'totalCost':totalCost,
                    'summarizedText': summary,
                    },200
        else:
            return {
                "success":False,
                "msg":"err in pdfSummary controller",
                "err":"quiz is empty"
            },400
    
    except Exception as e:
        print("errr ")
        return {
            "success":False,
            "msg":"err in controller/summary.py",
            "err":f"{e}"
        },400


def textSummaryController(text:str,tire:str,lang:str):
    
    try:

        # getting the number of charcter to use
        charctersLimit = FREE_TIRE_CHARACTERS_LIMIT if tire.lower()=='free' else PAIED_TIRE_CHARACTERS_LIMIT
            
        #limiting the text to the charctersLimit
        plainText = text.strip().replace('  ',' ').replace('\n',' ')[:charctersLimit]

        # creating the summaries
        summary, totalTokenUsed, totalCost = SummaryService(plainText,lang).getLangChainSummary()

        # returning the summaries to the user
        if summary:
                    
            return {'success': True,
                    'totalTokensUsed':totalTokenUsed,
                    'totalCost':totalCost,
                    'summarizedText': summary,
                    },200
        else:
            return {
                "success":False,
                "msg":"err in textSummary controller",
                "err":"summary is empty"
            },400
    
    except Exception as e:
        print("errr ")
        return {
            "success":False,
            "msg":"err in controller/summary.py",
            "err":f"{e}"
        },400

