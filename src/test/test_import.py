import os

from src.test.test_setup import ProjectTests
from src.data_manager import DataManager
from src.models import Store
from src import db


class TestImport(ProjectTests):

    def test_correct_number_imported(self):
        stores = db.session.query(Store).all()
        self.assertEquals(len(stores), 6)

    def test_no_duplicated(self):
        db_manage = DataManager()
        folder_path = os.path.dirname(os.path.abspath(__file__))
        db_manage.load_data(folder_path)

        stores = db.session.query(Store).all()
        self.assertEquals(len(stores), 6)
