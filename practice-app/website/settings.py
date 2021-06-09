import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")
API_KEY2 = os.environ.get("API_KEY2")
API_KEY_BADGE = os.environ.get("API_KEY_BADGE")
BASE_URL = os.environ.get("BASE_URL")