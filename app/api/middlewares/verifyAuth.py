import os
import dotenv
dotenv.load_dotenv()

def verifyAuth(authId):
    if authId == os.environ['AUTHID']:
        return True
    else:
        return False