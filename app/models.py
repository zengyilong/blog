import sqlite3
from contextlib import closing



def connect_db(config):
    return sqlite3.connect(config)


def init_db(app):
    with closing(connect_db(app.config['DATABASE'])) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()