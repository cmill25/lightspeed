import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv("API_TOKEN")

if api_token is None:
    raise ValueError("API_TOKEN not found in environment variables")
