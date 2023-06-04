
from app.api.utils import FREE_TIRE_CHARACTERS_LIMIT , PAIED_TIRE_CHARACTERS_LIMIT
from app.api.service.pdf import PdfService
from app.api.service.quiz import QuizService


def pdfQuizController(file,tire:str,lang:str):

    try:

        # getting the number of charcters to use
        charctersLimit = FREE_TIRE_CHARACTERS_LIMIT if tire.lower()=='free' else PAIED_TIRE_CHARACTERS_LIMIT

        # extracting plain text from the file
        plainText = PdfService(file,charctersLimit).getText()

        # creating the quiz
        quiz,totalTokenUsed,totalCost = QuizService(plainText,lang).getQuiz()

        # returning the quiz
        if quiz:
            return {'success': True,
                    'totalTokensUsed':totalTokenUsed,
                    'totalCost':totalCost,
                    'quiz': quiz,
                    },200
        else:
            return {
                "success":False,
                "msg":"err in pdfQuiz",
                "err":f"quiz is empty"
            },400
    
    except Exception as e:
       
        print("err at pdfQuiz controller")
        
        return {
            "success":False,
            "msg":"err in pdfQuizController",
            "err":f"{e}"
        },400
    



def textQuizController(text,tire:str,lang:str):
    
    try:
        
        # getting the number of charcter to use
        charctersLimit = FREE_TIRE_CHARACTERS_LIMIT if tire.lower()=='free' else PAIED_TIRE_CHARACTERS_LIMIT

        # limiting the text to the charctersLimit
        text = text.strip().replace('  ',' ').replace('\n',' ')[:charctersLimit]

        # creating the quiz
        quiz,totalTokenUsed,totalCost = QuizService(text,lang).getQuiz()

        # returning the quiz
        if quiz:
            return {'success': True,
                    'totalTokensUsed':totalTokenUsed,
                    'totalCost':totalCost,
                    'quiz': quiz,
                    },200
        else:
            return {
                "success":False,
                "msg":"err in textQuiz",
                "err":f"quiz is empty"
            },400
    
    except Exception as e:
       
        print("errr at pdfQuiz controller")
        
        return {
            "success":False,
            "msg":"err in textQuizController",
            "err":f"{e}"
        },400