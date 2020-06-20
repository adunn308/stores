from database import db
from geoalchemy2 import Geometry


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

    @classmethod
    def update_geometries(cls):
        """Using each city's longitude and latitude, add geometry data to db."""

        stores = Store.query.all()

        for store in stores:
            point = 'POINT({} {})'.format(store.longitude, store.latitude)
            store.geo = point

        db.session.commit()
