import os

import openai
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
SLEEP_SECONDS = 20
