from app import create_app
from app.models import init_db
from flask_bootstrap import Bootstrap


app = create_app()
bootstrap = Bootstrap(app)

if __name__ == '__main__':
    init_db(app)
    app.run()
