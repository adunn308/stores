import requests

from geoalchemy2 import functions, Geometry

from models import Store
from config import EnvConfig


class StoresObject(object):
    def __init__(self):
        self.config = EnvConfig()

    def list_stores(self):
        sorted_stores = Store.query.order_by(Store.name).all()
        return sorted_stores

    def check_stores(self, postcode, distance):
        centre_long_lat, error_message = self.postcode_long_lat(postcode)
        radius = distance
        if not error_message:
            point = functions.ST_Point(centre_long_lat[0], centre_long_lat[1])

            results = Store.query.filter(functions.ST_DistanceSphere(Store.geo, point) < radius)\
                                 .order_by(Store.latitude.desc()).all()
        else:
            results = []
        return results, error_message

    def postcode_long_lat(self, postcode):
        postcodes_url = f"{self.config.postcodes_api}/postcodes/{postcode}"
        try:
            resp = requests.get(postcodes_url)
            resp.raise_for_status()
            json_resp = resp.json()
            longitude = json_resp['result']['longitude']
            latitude = json_resp['result']['latitude']
            return (longitude, latitude), None
        except Exception as e:
            print(e)
            error_message = "Could not find details on this postcode, please check it is valid or try again later"
            return None, error_message

