from flask import Flask
import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
import app


app = Flask(__name__)
db = SQLAlchemy(app)

def create_app():

    app.config.from_object(config)
    bootstrap = Bootstrap(app)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    db.init_app(app)
    db.create_all()
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app


