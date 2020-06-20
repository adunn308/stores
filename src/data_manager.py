import os
import json
import requests

from requests.exceptions import HTTPError
from sqlalchemy.ext.declarative import declarative_base

from config import EnvConfig
from models import Store
from database import db


Base = declarative_base()


class DataManager(object):
    def __init__(self):
        self.config = EnvConfig()

    def load_data(self, folder_path):
        path_to_data = os.path.join(folder_path, 'data/stores.json')
        data = json.load(open(path_to_data))
        for store in data:
            existing_record = db.session.query(Store).filter_by(name=store['name'], postcode=store['postcode']).first()
            if existing_record:
                continue
            else:
                new_record = Store(name=store['name'], postcode=store['postcode'])
                record = self.get_lat_lon(new_record)
                if not record:
                    continue
                db.session.add(record)
        Store.update_geometries()
        db.session.commit()

    def get_lat_lon(self, record):
        postcodes_url = f"{self.config.postcodes_api}/postcodes/{record.postcode}"
        try:
            resp = requests.get(postcodes_url)
            resp.raise_for_status()
            updated_record = self._fetch_data_from_resp(resp, record)
        except HTTPError:
            updated_record = self.try_expired(record)
        except Exception as e:
            print(f"failed to find lat/lon on postcodes.io. Error msg: {e}")
            return None
        return updated_record

    def try_expired(self, record):
        try:
            expired_url = f"{self.config.postcodes_api}/terminated_postcodes/{record.postcode}"
            resp = requests.get(expired_url)
            resp.raise_for_status()
            updated_record = self._fetch_data_from_resp(resp, record)
            return updated_record
        except Exception as e:
            print(f"failed to find lat/lon. Error msg: {e}")
            return None

    def _fetch_data_from_resp(self, resp, record):
        json_resp = resp.json()
        longitude = json_resp['result']['longitude']
        latitude = json_resp['result']['latitude']
        record.longitude = longitude
        record.latitude = latitude
        return record
