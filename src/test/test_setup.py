import os
import unittest

from src.data_manager import DataManager
from src import app, db


class ProjectTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        db.create_all()
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db_manage = DataManager()
        folder_path = os.path.dirname(os.path.abspath(__file__))
        db_manage.load_data(folder_path)

    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


if __name__ == "__main__":
    unittest.main()
