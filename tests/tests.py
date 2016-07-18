# -*- coding:utf-8 -*-
import os
import runapp
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, runapp.app.config['DATABASE'] = tempfile.mkstemp()
        runapp.app.config['TESTING'] = True
        self.app = runapp.app.test_client()
        runapp.init_db(runapp.app)

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(runapp.app.config['DATABASE'])

    # 访问应用根节点应出现 “No entries here so far”
    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    def login(self, username, password):
         return self.app.post('/login', data=dict(username=username,password=password),
                              follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    # 测试登录及日志输入输出
    def test_login_logout(self):
        rv = self.login('admin', '123456')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data

    # 测试添加功能
    def test_messages(self):
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