from applications.view.admin import init_admin_views
from applications.view.index import init_index_views


def init_view(app):
    init_admin_views(app)
    init_index_views(app)
