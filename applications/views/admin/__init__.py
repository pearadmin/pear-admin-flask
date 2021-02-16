from applications.views.admin.index import admin_index
from applications.views.admin.user import admin_user


def init_adminViews(app):
    """
    初始化蓝图

    """

    app.register_blueprint(admin_index)
    app.register_blueprint(admin_user)
