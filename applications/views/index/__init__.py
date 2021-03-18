from applications.views.index.index import index_index


def init_indexViews(app):
    """
    初始化蓝图

    """

    app.register_blueprint(index_index)
