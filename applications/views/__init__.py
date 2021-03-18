from applications.views.admin import init_adminViews
from applications.views.index import init_indexViews


def init_view(app):
    init_adminViews(app)
    init_indexViews(app)
