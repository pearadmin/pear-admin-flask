from flask import Flask

from .init_databases import register_script
from .init_sqlalchemy import db, ma, init_databases
from .init_login import init_login_manager
from .init_debug_tool import init_debug_tool
from .init_template_directives import init_template_directives
from .init_error_views import init_error_views


def init_plugs(app: Flask) -> None:
    # init_debug_tool(app)
    init_login_manager(app)
    init_databases(app)
    init_template_directives(app)
    init_error_views(app)
    register_script(app)
