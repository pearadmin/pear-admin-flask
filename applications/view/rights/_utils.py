import copy
from collections import OrderedDict

from flask import current_app
from flask_login import current_user
from flask_restful import marshal

from applications.common.serialization import power_fields
from applications.extensions import db
from applications.models import Power, Role, User

from applications.common.serialization import power2_fields


def get_render_config():
    # 网站配置
    config = dict(logo={
        # 网站名称
        "title": current_app.config.get("SYSTEM_NAME"),
        # 网站图标
        "image": "/static/admin/admin/images/logo.png"
        # 菜单配置
    }, menu={
        # 菜单数据来源
        "data": "/rights/menu",
        "collaspe": True,
        # 是否同时只打开一个菜单目录
        "accordion": True,
        "method": "GET",
        # 是否开启多系统菜单模式
        "control": False,
        # 默认选中的菜单项
        "select": "0",
        # 是否开启异步菜单，false 时 data 属性设置为菜单数据，false 时为 json 文件或后端接口
        "async": True
    }, tab={
        # 是否开启多选项卡
        "muiltTab": True,
        # 切换选项卡时，是否刷新页面状态
        "keepState": True,
        # 是否开启 Tab 记忆
        "session": True,
        # 最大可打开的选项卡数量
        "tabMax": 30,
        "index": {
            # 标识 ID , 建议与菜单项中的 ID 一致
            "id": "10",
            # 页面地址
            "href": "/admin/welcome",
            # 标题
            "title": "首页"
        }
    }, theme={
        # 默认主题色，对应 colors 配置中的 ID 标识
        "defaultColor": "2",
        # 默认的菜单主题 dark-theme 黑 / light-theme 白
        "defaultMenu": "dark-theme",
        # 是否允许用户切换主题，false 时关闭自定义主题面板
        "allowCustom": True
    }, colors=[{
        "id": "1",
        "color": "#2d8cf0"
    },
        {
            "id": "2",
            "color": "#5FB878"
        },
        {
            "id": "3",
            "color": "#1E9FFF"
        }, {
            "id": "4",
            "color": "#FFB800"
        }, {
            "id": "5",
            "color": "darkgray"
        }
    ], links=current_app.config.get("SYSTEM_PANEL_LINKS"), other={
        # 主页动画时长
        "keepLoad": 1200,
        # 布局顶部主题
        "autoHead": False
    }, header=False)
    return config


# 生成菜单树
def make_menu_tree():
    role = current_user.role
    powers = []
    for i in role:
        # 如果角色没有被启用就直接跳过
        if i.enable == 0:
            continue
        # 变量角色用户的权限
        for p in i.power:
            # 如果权限关闭了就直接跳过
            if p.enable == 0:
                continue
            # 一二级菜单
            if p.type == 0 or p.type == 1:
                powers.append(p)

    power_dict = marshal(powers, power2_fields)  # 生成可序列化对象
    power_dict.sort(key=lambda x: x['id'], reverse=True)

    menu_dict = OrderedDict()
    for _dict in power_dict:
        if _dict['id'] in menu_dict:
            # 当前节点添加子节点
            _dict['children'] = copy.deepcopy(menu_dict[_dict['id']])
            # 删除子节点
            del menu_dict[_dict['id']]

        if _dict['parent_id'] not in menu_dict:
            menu_dict[_dict['parent_id']] = [_dict]
        else:
            menu_dict[_dict['parent_id']].append(_dict)
    return menu_dict.get(0)


# 选择父节点
def select_power_dict():
    power = Power.query.all()
    res = marshal(power, power_fields)
    res.append({"powerId": 0, "powerName": "顶级权限", "parentId": -1})
    return res


def get_power_dict():
    power = Power.query.all()
    res = marshal(power, power_fields)
    return res


# 删除权限（目前没有判断父节点自动删除子节点）
def remove_power(power_id):
    power = Power.query.filter_by(id=power_id).first()
    role_id_list = []
    roles = power.role
    for role in roles:
        role_id_list.append(role.id)
    roles = Role.query.filter(Role.id.in_(role_id_list)).all()
    for p in roles:
        power.role.remove(p)
    r = Power.query.filter_by(id=power_id).delete()
    db.session.commit()
    return r


# 批量删除权限
def batch_remove_power(ids):
    for _id in ids:
        remove_power(_id)


def remove_role(_id):
    """ 删除角色 """
    role = Role.query.filter_by(id=_id).first()
    # 删除该角色的权限
    power_id_list = []
    for p in role.power:
        power_id_list.append(p.id)

    powers = Power.query.filter(Power.id.in_(power_id_list)).all()
    for p in powers:
        role.power.remove(p)
    user_id_list = []
    for u in role.user:
        user_id_list.append(u.id)
    users = User.query.filter(User.id.in_(user_id_list)).all()
    for u in users:
        role.user.remove(u)
    r = Role.query.filter_by(id=_id).delete()
    db.session.commit()
    return r


def batch_remove_role(ids):
    """ 批量删除 """
    for _id in ids:
        remove_role(_id)
