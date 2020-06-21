import os


POSTGRES_URL = os.getenv("POSTGRES_URL", "127.0.0.1:5432")
POSTGRES_USER = os.getenv("POSTGRES_USER", "")
POSTGRES_PASS = os.getenv("POSTGRES_PW", "")
POSTGRES_DB = "test_stores"
SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_URL}/{POSTGRES_DB}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

POSTCODES_API = "https://api.postcodes.io"

DEBUG = False
TESTING = True