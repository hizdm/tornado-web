# tornado-web

A Python Web Frame Based Tornado！

# [目录]

```shell
.
├── app.py               # 项目入口文件
├── conf                 # 配置文件目录
│ └── global.ini         # 基础配置文件
├── controller           # 控制层
│ ├── base.py            # 控制层基类
│ └── test.py            # 控制层测试类
├── library              # 基础类库
│ ├── jwt                # JWT验证基类
│ │ └── jwt.py
│ ├── log                # 日志操作基类
│ │ └── loghelper.py
│ ├── mysql              # MySQL操作基类
│ │ └── mysqlhelper.py
│ ├── redis              # Redis操作基类
│ │ └── redishelper.py
│ └── util               # 公共方法工具
│ └── util.py
├── log                  # 日志存放目录
│ └── log.txt
├── model                # 模型层
│ ├── base.py            # 模型基类
│ └── test.py            # 模型测试类
├── README.md
├── requirements.txt     # 框架安装包 pip install -r requirements.txt
├── router               # 路由分发层
│ └── urls.py            # 路由分发文件 
├── static               # 资源层
└── template             # 模板层
 └── 404.html            # 404页面
```

# [准备]

安装依赖包`pip install -r requirements.txt`
