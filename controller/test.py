# -*- coding: utf-8 -*-
import tornado.web
import sys

"""
测试模块Index控制层
"""
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Test Index Handler')
        #self.render("test.html")
