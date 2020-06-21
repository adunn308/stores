from flask import Flask
from sqlalchemy_utils import database_exists, create_database
import os

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'TEST':
    app.config.from_object('test_config')
else:
    app.config.from_object('config')

db = SQLAlchemy(app)
db.init_app(app)

# create the db if it doesn't exist. Added to make running tech test easier!
if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    print("db exists")
if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    print("creating db")
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])

from .database import init_db  # noqa E402
with app.app_context():
    init_db(db)

# import blueprints and routes
from src import routes  # noqa E402
app.register_blueprint(routes.mod)
