from app.models import User,Role,Entry
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from app import app, db


db.drop_all()
db.create_all()

admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')

entry_no1 = Entry(title= 'hi',text = 'nihao')
e1 = Entry(title='hahah',text='heihei')
print(admin_role.id)

print(mod_role.id)

print(user_role.id)

print(entry_no1.id)
db.session.add_all([admin_role, mod_role, user_role, entry_no1,e1])
db.session.commit()
print(admin_role.id)

print(mod_role.id)

print(user_role.id)

print(entry_no1.id)

find = Role.query.all()
for i in find:
    print i

entr = [dict(title = row[0]) for row in Role.query.all()]
print entr
for j in entr:
    print 'entr first'
    print j.text
    print 'entr end'