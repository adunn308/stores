import os
import unittest

from sqlalchemy_utils import database_exists, create_database, drop_database

from app import app
from database import db
from data_manager import DataManager
from config import EnvConfig


class ProjectTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        config = EnvConfig()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = config.test_db

        if database_exists(config.test_db):
            print("test db exists")
        if not database_exists(config.test_db):
            print("creating test db")
            create_database(config.test_db)
        db.session.close()

        db.engine.execute("CREATE EXTENSION IF NOT EXISTS postgis")
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        db_manage = DataManager()
        folder_path = os.path.dirname(os.path.abspath(__file__))
        db_manage.load_data(folder_path)

    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == "__main__":
    unittest.main()
