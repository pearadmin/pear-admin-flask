from flask import Flask

from .init_databases import register_script
from .init_sqlalchemy import db, init_databases
from .init_login import init_login_manager
from .init_template_directives import init_template_directives
from .init_error_views import init_error_views


def init_plugs(app: Flask) -> None:
    init_login_manager(app)
    init_databases(app)
    init_template_directives(app)
    init_error_views(app)

    # 生成测试数据的命令，生成环境可以注释
    register_script(app)
