from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = getenv("API_TOKEN", "")
if API_TOKEN is "":
    raise ValueError("API_TOKEN is not set")

GOOGLE_TOKEN = getenv("GOOGLE_TOKEN", "")
if GOOGLE_TOKEN is "":
    raise ValueError("GOOGLE_TOKEN is not set")
