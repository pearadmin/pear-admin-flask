from flask import Flask

from .department import dept_bp
from .file import file_bp
from .index import index_bp
from .logs_view import logs_bp
from .passport import passport_bp
from .rights import rights_bp
from .roles import role_bp
from .users import users_bp


def init_view(app: Flask):
    app.register_blueprint(dept_bp)
    app.register_blueprint(file_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(logs_bp)
    app.register_blueprint(passport_bp)
    app.register_blueprint(rights_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(users_bp)
