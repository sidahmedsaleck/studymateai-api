import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('.env'))
from app.api.utils import CHUNK_OVERLAP, CHUNK_SIZE, QUIZ_PROMPTS
from langchain import OpenAI, PromptTemplate
from langchain.callbacks import get_openai_callback
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import json

class QuizService:

    def __init__(self, text, language="en"):
        self._text = text
        self._language = language
        self._llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"],max_tokens=2000)
        self._text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)
        self._quiz = None
        self._totalTokensUsed = None
        self._totalCost = None
    
    def getQuiz(self):
        """
            Return the quiz on the text.
            return:
            quiz: String (the quiz on the text)
            totalTokensUsed: int (the total tokens used to generate the quiz)
            totalCost: int (the total cost of the quiz)
        """
        quiz, tokensUsed = self.__getQuiz()
        totalTokensUsed = tokensUsed.completion_tokens + tokensUsed.prompt_tokens
        totalCost = tokensUsed.total_cost
        
        self._quiz = quiz
        self._totalTokensUsed = totalTokensUsed
        self._totalCost = totalCost
        
        return quiz,totalTokensUsed, totalCost 

    def printQuiz(self,quiz):
        for q in quiz:
            print(q,"\n\n")
    
    def __getQuiz(self):

        """
        we chunk the text into smaller pieces and then we generate a quiz for each chunk.
        combine the final result into one quiz.
        """
        PROMPT = PromptTemplate(template=QUIZ_PROMPTS[self._language], input_variables=["text"])
        textList = [ self._text ]
        document = [Document(page_content=t) for t in textList]
        docs = self._text_splitter.split_documents(document)


        with get_openai_callback() as tokensUsed:
            finalQuiz = []
            for d in docs:
                quiz = self._llm(PROMPT.format(text=d.page_content))
                # print("\n\n----\n",quiz,"\n\n----\n")
                # print(json.loads(quiz))
                quizSeriable =json.loads(quiz) 
                for q in quizSeriable:
                    finalQuiz.append(quizSeriable[q])

        return finalQuiz, tokensUsed