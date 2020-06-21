from geoalchemy2 import Geometry

from src import db


class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.Text(), nullable=False)
    postcode = db.Column(db.Text(), nullable=False)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    geo = db.Column(Geometry(geometry_type="POINT"))

    __table_args__ = (db.UniqueConstraint('name', 'postcode', name='_name_postcode_uc'),)

    def __repr__(self):
        return "<City {name} ({lat}, {lon})>".format(
            name=self.name, lat=self.latitude, lon=self.longitude)

    def update_geometry(self):
        point = 'POINT({} {})'.format(self.longitude, self.latitude)
        self.geo = point
