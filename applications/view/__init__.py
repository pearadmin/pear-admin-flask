from flask import Flask

from applications.view.admin import init_admin_views
from applications.view.index import init_index_views


def init_view(app: Flask):
    init_admin_views(app)
    init_index_views(app)

    # # 重定向到后台管理首页
    # @app.route('/')
    # def redirect_index():
    #     return redirect('/admin/login')
