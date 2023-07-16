
from io import BufferedReader, BytesIO
import re
from pdfplumber import PDF
from app.api.utils import FREE_TIRE_CHARACTERS_LIMIT






class PdfService:
    
    _pdfObject:PDF = None
    _charctersLimit:int= None

    def __init__(self, pdfFileBuffer:BufferedReader or BytesIO, charctersLimit=FREE_TIRE_CHARACTERS_LIMIT):
        self._pdfObject = PDF(pdfFileBuffer)
        self._charctersLimit = charctersLimit
        

    def getText(self):
        """
            Return the plain text in the pdf file.
            return:
            text: String (the plain text in the pdf)
        """
        text = self.__extractTextFromPdf()
        return text
    
    
    def __extractAlphanumeric(self,text):
        """
            Apply regx to eleminate unwanted charcters.
            return :
            newText: String (the alphanumeric text)
        """


        newText = re.sub('[^a-zA-Z0-9\nÀ-ÖØ-öø-ÿ\.\,\'\?\:\;\-\s]+', ' ', text)
        newText = re.sub(' +',' ',newText)
        newText = re.sub('\n+','\n',newText)
        
        return newText 
    
    
    def __extractTextFromPdf(self):
        """
        Read the .pdf file and return the plain text in that file.
        filePath: the path of the pdf file
        return:
        text = String (the plain text in the pdf)
        """

        filePages = self._pdfObject.pages
        text = ""
        for page in filePages:
            text = text +  self.__extractAlphanumeric(page.extract_text())
            if len(text) >= self._charctersLimit:
                break
        return text[:self._charctersLimit]