# -*- coding: utf-8 -*-
# Author: zzl
# Date: 2024.07.15

from __future__ import absolute_import
import os
import tornado.ioloop
import tornado.web
from tornado.options import options, define
import tornado.autoreload
import router.urls as urls
from library.util import util

define('port', default=int(util.fetch_conf('global.ini', 'app', 'port')), help='监听端口')
define('debug', default=util.fetch_conf('global.ini', 'app', 'debug'), help='是否开启调试') 

"""
@brief 404
"""
class My404Handler(tornado.web.RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.render('404.html')

def main():
    options.parse_command_line()
    app = tornado.web.Application(
        urls.urls, # 路由分发
        template_path=os.path.join(os.path.dirname(__file__), "template"), # 模板存放位置
        static_path=os.path.join(os.path.dirname(__file__), "static"), # 静态文件存放位置
        debug=options.debug, # 热加载调试（True:开启; False:关闭）
        default_handler_class=My404Handler) # 默认404
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()