import os
from dotenv import find_dotenv, load_dotenv

find_dotenv()
load_dotenv()

SECRET_KEY = os.getenv('SECRET')
ANSWER_API_URL = 'https://yesno.wtf/api'
