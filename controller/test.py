# -*- coding: utf-8 -*-
import sys
from controller.base import BaseHandler
from model.test import TestModel

"""
测试模块Index控制层
"""
class IndexHandler(BaseHandler):
    def get(self):
        # JWT认证
        # auth_token = self.getHeaders()
        # print(auth_token)
        # if not auth_token:
        #     return
        # uid = auth_token.get('payload')
        # print(uid)
        

        # 数据前端数据记录页面渲染
        # self.write('Test Index Handler')
        # #self.render("test.html")

        # 获取单条数据
        test_instance = TestModel('global.ini', 'mysql_w')
        result = test_instance.fetchOne('select * from wiki_contents where cid = %s', [4])
        print(result)