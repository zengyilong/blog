# -*- coding:utf-8 -*-
from flask import current_app
from app import db, create_app
import unittest
import tempfile


class BolgTestCase(unittest.TestCase):

    def setUp(self):
        #self.db_fd, runapp.app.config['DATABASE'] = tempfile.mkstemp()
        # self.app = runapp.app.test_client()
        # runapp.init_db(runapp.app)
        # app = create_app()
        # app.config['TESTING'] = True
        # db.drop_all()
        # db.init_app(app)
        # db.create_all()
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        db.create_all()


    def tearDown(self):
        # os.close(self.db_fd)
        # os.unlink(runapp.app.config['DATABASE'])
        db.session.remove()
        db.drop_all()
        self.app_context.pop()



    # 测试应用成功启动
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # 测试应用是否为测试状态
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])


    # 访问应用根节点应出现 “No entries here so far”
    def test_empty_db(self):
        rv = self.client.get('/')
        assert 'No entries here so far' in rv.data

    def login(self, username, password):
         return self.client.post('/login', data=dict(username=username,password=password),
                              follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    # 测试登录及日志输入输出
    def t_est_login_logout(self):
        rv = self.login('admin', '123456')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data

    # 测试添加功能
    def t_est_messages(self):
        self.login('admin', '123456')
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data

if __name__ == '__main__':
    unittest.main()