
from app.api.utils import FREE_TIRE_CHARACTERS_LIMIT , PAIED_TIRE_CHARACTERS_LIMIT
from app.api.service.pdf import PdfService
from app.api.service.flashcards import FlashcardsService


def pdfFlashcardsController(file,tire:str,lang:str):

    try:

        # getting the number of charcters to use
        charctersLimit = FREE_TIRE_CHARACTERS_LIMIT if tire.lower()=='free' else PAIED_TIRE_CHARACTERS_LIMIT

        # extracting plain text from the file
        plainText = PdfService(file,charctersLimit).getText()

        # creating the flashcards
        flashcards,totalTokenUsed,totalCost = FlashcardsService(plainText,lang).getFlashcards()

        # returning the flashcards
        if flashcards:
            return {'success': True,
                    'totalTokensUsed':totalTokenUsed,
                    'totalCost':totalCost,
                    'flashcards': flashcards,
                    },200
        else:
            return {
                "success":False,
                "msg":"err in pdfFlashcards",
                "err":f"flashcards is empty"
            },400
    
    except Exception as e:
       
        print("err at pdfFlashcards controller")
        
        return {
            "success":False,
            "msg":"err in pdfFlashcardsController",
            "err":f"{e}"
        },400
    



def textFlashcardsController(text,tire:str,lang:str):
    
    try:

        # getting the number of charcter to use
        charctersLimit = FREE_TIRE_CHARACTERS_LIMIT if tire.lower()=='free' else PAIED_TIRE_CHARACTERS_LIMIT

        # limiting the text to the charctersLimit
        text = text.strip().replace('  ',' ').replace('\n',' ')[:charctersLimit]

        # creating the flashcards
        flashcards,totalTokenUsed,totalCost = FlashcardsService(text,lang).getFlashcards()

        # returning the flashcards
        if flashcards:
            return {'success': True,
                    'totalTokensUsed':totalTokenUsed,
                    'totalCost':totalCost,
                    'flashcards': flashcards,
                    },200
        else:
            return {
                "success":False,
                "msg":"err in textflashcards",
                "err":f"flashcards is empty"
            },400
    
    except Exception as e:
       
        print("errr at TextFlashcards controller")
        
        return {
            "success":False,
            "msg":"err in TextFlashcardsController",
            "err":f"{e}"
        },400