# -*- coding:utf-8 -*-
from app import create_app
#from app.models import init_db
from flask_bootstrap import Bootstrap
from app import db
from app.models import Role,User,Entry
# app = create_app()
# bootstrap = Bootstrap(app)



if __name__ == '__main__':
    #测试代码
    app = create_app()
    db.drop_all()
    db.init_app(app)
    db.create_all()
    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_admin = User(username='admin', password='123456')
    e1 = Entry(title='hahah',text='heihei')
    db.session.add_all([admin_role, mod_role, user_role, user_admin, e1])
    db.session.commit()
    user = User.query.filter_by(username='admin').first()
    print user.username
    print user.password
    #测试代码
    #init_db(app)
    #db.create_all()

    app.run(debug=True)
