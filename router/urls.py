# -*- coding: utf-8 -*-
# Author: zzl
# Date: 2024.07.15

from controller import test # 引入测试模块

# 路由设置
urls = [
    (r"/", test.IndexHandler)
]
