import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("HOST_ENTITY_USERNAME")
PASSWORD = os.getenv("HOST_ENTITY_PASSWORD")
