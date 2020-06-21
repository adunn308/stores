import os

from flask import render_template, Blueprint

from src.get_stores import GetStores
from src.data_manager import DataManager


mod = Blueprint('routes', __name__)


@mod.route('/')
def index():
    return 'Not Available, please try "/load_data", "/stores" or "/find_stores/<postcode>/<distance in m>"'


@mod.route('/load_data')
def load_data():
    db_manage = DataManager()
    folder_path = os.path.dirname(os.path.abspath(__file__))
    db_manage.load_data(folder_path)
    return "data loaded"


@mod.route('/stores')
def stores():
    stores_object = GetStores()
    info = stores_object.list_stores()
    return render_template('stores.html', info=info)


@mod.route('/find_stores/<postcode>/<distance>', methods=['GET'])
def find_stores(postcode, distance):
    stores_object = GetStores()
    result, error_message = stores_object.find_stores(postcode, distance)
    return render_template('radius.html',
                           results=result,
                           radius=distance,
                           postcode=postcode,
                           error_message=error_message)
