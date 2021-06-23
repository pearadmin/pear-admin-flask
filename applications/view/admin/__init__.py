from flask import Flask

from applications.view.admin.admin_log import admin_log
from applications.view.admin.dict import admin_dict
from applications.view.admin.index import admin_bp
from applications.view.admin.file import admin_file
from applications.view.rights.role import admin_role
from applications.view.company.users import users_bp
from applications.view.admin.monitor import admin_monitor_bp


def register_admin_views(app: Flask):
    app.register_blueprint(admin_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(admin_file)
    app.register_blueprint(admin_monitor_bp)
    app.register_blueprint(admin_log)
    app.register_blueprint(admin_role)
    app.register_blueprint(admin_dict)
