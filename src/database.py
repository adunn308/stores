from src.models import Store  # noqa F401


def init_db(db):
    db.engine.execute("CREATE EXTENSION IF NOT EXISTS postgis")
    db.create_all()
    db.session.commit()
