import os

from flask import Flask, render_template
from sqlalchemy_utils import database_exists, create_database, drop_database

from database import db
from config import EnvConfig
from data_manager import DataManager
from stores_object import StoresObject

from models import Store  # noqa: F401

app = Flask(__name__)
app.debug = True
config = EnvConfig()
app.config['SQLALCHEMY_DATABASE_URI'] = config.db_url
db.app = app
db.init_app(app)

if database_exists(config.db_url):
    print("db exists")
if not database_exists(config.db_url):
    print("creating db")
    create_database(config.db_url)
db.engine.execute("CREATE EXTENSION IF NOT EXISTS postgis")
db.create_all()
db.session.commit()


@app.route('/')
def index():
    return 'hello world'


@app.route('/load_data')
def load_data():
    db_manage = DataManager()
    folder_path = os.path.dirname(os.path.abspath(__file__))
    db_manage.load_data(folder_path)
    return "data loaded"


@app.route('/stores')
def stores():
    stores_object = StoresObject()
    info = stores_object.list_stores()
    return render_template('stores.html', info=info)


@app.route('/check_stores/<postcode>/<distance>', methods=['GET'])
def check_stores(postcode, distance):
    stores_object = StoresObject()
    result, error_message = stores_object.check_stores(postcode, distance)
    return render_template('radius.html', results=result, radius=distance, postcode=postcode,
                           error_message=error_message)


if __name__ == '__main__':
    app.run()
