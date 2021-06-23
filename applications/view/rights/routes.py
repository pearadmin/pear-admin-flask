# 渲染配置
from flask import jsonify
from flask_login import login_required

from . import rights_bp

from ._utils import get_render_config, make_menu_tree


@rights_bp.get('/configs')
@login_required
def configs():
    return get_render_config()


# 菜单
@rights_bp.get('/menu')
@login_required
def menu():
    menu_tree = make_menu_tree()
    return jsonify(menu_tree)
