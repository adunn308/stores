import os


class EnvConfig(object):
    def __init__(self):
        self.postgres_url = os.getenv("POSTGRES_URL", "127.0.0.1:5432")
        self.postgres_user = os.getenv("POSTGRES_USER", "")
        self.postgres_pass = os.getenv("POSTGRES_PW", "")
        self.postgres_db = os.getenv("POSTGRES_DB", "stores")
        self.db_url = f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_pass}@{self.postgres_url}/{self.postgres_db}"
        self.postgres_test_db = 'test_stores'
        self.test_db = f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_pass}@{self.postgres_url}/{self.postgres_test_db}"
        self.postcodes_api = "https://api.postcodes.io"
