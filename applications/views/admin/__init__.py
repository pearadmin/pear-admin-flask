from applications.views.admin.index import admin_index
from applications.views.admin.user import admin_user
from applications.views.admin.file import admin_file
from applications.views.admin.monitor import admin_Monitor
from applications.views.admin.admin_log import admin_log
from applications.views.admin.power import admin_power
from applications.views.admin.role import admin_role
from applications.views.admin.dict import admin_dict
"""
   初始化蓝图

   """


def init_adminViews(app):

    app.register_blueprint(admin_index)
    app.register_blueprint(admin_user)
    app.register_blueprint(admin_file)
    app.register_blueprint(admin_Monitor)
    app.register_blueprint(admin_log)
    app.register_blueprint(admin_power)
    app.register_blueprint(admin_role)
    app.register_blueprint(admin_dict)

