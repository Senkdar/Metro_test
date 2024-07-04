import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

PARSING_HEADERS = {"User-Agent": "Chrome/91.0.4472.124"}

IMAGE_PREFIX = "https://mosday.ru/news/"

METRO_SITE_URL = "http://mosday.ru/news/tags.php?metro"

MINUTES_TO_START_PARSING = 10
