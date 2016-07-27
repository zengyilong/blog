from flask import Flask
import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
import app


app = Flask(__name__)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
db.init_app(app)
db.create_all()

def create_app():
    app.config.from_object(config)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # import blueprint here
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app


