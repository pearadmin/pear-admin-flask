from flask import Flask
from flask_uploads import configure_uploads, patch_request_class
from applications.config import database, common
from applications.models import db
from applications.service.debug_tool import open_debug_tool
from applications.service.login import init_flask_login
from applications.service.upload import photos
from applications.views import init_view
from applications.views.admin.context_processor import init_template_global
from applications.views.admin.error import init_error


def create_app():
    app = Flask(__name__)
    # 注册路由
    init_view(app)
    # 注册错误页面
    init_error(app)
    # 注册自定义上下文函数
    init_template_global(app)
    # 引入数据库配置
    app.config.from_object(database)
    app.config.from_object(common)
    # sqlalchemy初始化
    db.init_app(app)
    # flask_login初始化
    init_flask_login(app)
    # 文件上传
    configure_uploads(app, photos)
    patch_request_class(app)
    # 调试工具栏
    open_debug_tool(app)
    # logo
    logo()
    return app


def logo():
    print('''
 _____                              _           _         ______ _           _    
|  __ \                    /\      | |         (_)       |  ____| |         | |   
| |__) |__  __ _ _ __     /  \   __| |_ __ ___  _ _ __   | |__  | | __ _ ___| | __
|  ___/ _ \/ _` | '__|   / /\ \ / _` | '_ ` _ \| | '_ \  |  __| | |/ _` / __| |/ /
| |  |  __/ (_| | |     / ____ \ (_| | | | | | | | | | | | |    | | (_| \__ \   < 
|_|   \___|\__,_|_|    /_/    \_\__,_|_| |_| |_|_|_| |_| |_|    |_|\__,_|___/_|\_\\
    
    ''')


app = create_app()
