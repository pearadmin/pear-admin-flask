from flask import Flask

from applications.view.admin.logs import admin_log
from applications.view.admin.index import admin_bp
from applications.view.admin.file import file_bp
from applications.view.rights.role import role_bp
from applications.view.company.users import users_bp
from applications.view.admin.monitor import admin_monitor_bp


def register_admin_views(app: Flask):
    app.register_blueprint(admin_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(file_bp)
    app.register_blueprint(admin_monitor_bp)
    app.register_blueprint(admin_log)
    app.register_blueprint(role_bp)
