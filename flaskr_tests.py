# -*- coding: utf-8 -*-
# @Time     : 2018/4/16 21:33
# @Author   : Narata
# @File     : flaskr_tests.py
# @Software : PyCharm

import os
import flaskr
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):
    
    # 创建一个新的客户端，并初始化一个新的数据库
    # 每个独立的测试函数运行前都会调用该方法
    def setUp(self):
        flaskr.app.config['DATABASE'] = tempfile.mkdtemp() + '.db'
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()
        
    # 在测试结束后关闭文件，并在文件系统中删除数据库文件
    def tearDown(self):
        # os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'No entries here so far' in rv.data


if __name__ == '__main__':
    unittest.main