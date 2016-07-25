from . import main
from flask import g,render_template,flash,session,abort,request,redirect,url_for
from ..models import User,Entry,db


@main.before_request
def before_request():
    pass


@main.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@main.route('/')
def show_entries():
    test = Entry.query.all()
    print test
    entries = Entry.query.all()
    return render_template('show_entries.html', entries=entries)


@main.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    newentry = Entry(title=request.form['title'], text=request.form['text'])
    db.session.add_all([newentry])
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('main.show_entries'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username='admin').first()
        if user == None:
            error = 'Invalid username'
        elif request.form['password'] != user.password:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('main.show_entries'))
    return render_template('login.html', error=error)


@main.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('main.show_entries'))

