from flask import Flask

from applications.view.system.logs import admin_log
from applications.view.system.index import admin_bp
from applications.view.upload.file import file_bp
from applications.view.roles.role import role_bp
from applications.view.users import users_bp


def register_system_views(app: Flask):
    app.register_blueprint(admin_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(file_bp)
    app.register_blueprint(admin_log)
    app.register_blueprint(role_bp)
