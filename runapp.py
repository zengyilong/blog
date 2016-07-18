from app import create_app
from app.models import init_db

app = create_app()

def testprint():
    print "print..."


if __name__ == '__main__':
    init_db(app)
    app.run()
