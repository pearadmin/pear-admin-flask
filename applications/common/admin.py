from io import BytesIO
from flask import session, make_response, current_app
from flask_login import current_user

from applications.common.utils.gen_captcha import gen_captcha
from applications.schemas import PowerSchema


# 授权路由存入session
def add_auth_session():
    role = current_user.role
    user_power = []
    for i in role:
        if i.enable == 0:
            continue
        for p in i.power:
            if p.enable == 0:
                continue
            user_power.append(p.code)
    session['permissions'] = user_power


# 生成菜单树
def make_menu_tree():
    # power0 = Power.query.filter(
    #     Power.type == 0,
    # ).all()
    # power1 = Power.query.filter(
    #     Power.type == 1
    # ).all()
    # 获取当前用户的角色
    role = current_user.role
    power0 = []
    power1 = []
    for i in role:
        # 如果角色没有被启用就直接跳过
        if i.enable == 0:
            continue
        # 变量角色用户的权限
        for p in i.power:
            # 如果权限关闭了就直接跳过
            if p.enable == 0:
                continue
            # 一级菜单
            if int(p.type) == 0:
                power0.append(p)
            # 二级菜单
            else:
                power1.append(p)

    power_schema = PowerSchema(many=True)  # 用已继承 ma.ModelSchema 类的自定制类生成序列化类
    power0_dict = power_schema.dump(power0)  # 生成可序列化对象
    power1_dict = power_schema.dump(power1)  # 生成可序列化对象
    power0_dict = sorted(power0_dict, key=lambda i: i['sort'])
    power1_dict = sorted(power1_dict, key=lambda i: i['sort'])
    # print(power0)
    # print(power1)

    menu = []

    for p0 in power0_dict:
        for p1 in power1_dict:
            for p2 in power1_dict:
                if p1.get('id') == p2.get('parent_id') and int(p2.get('type'))<2:
                    if p1.get("children") is None:
                        p1['children'] = []
                        p1['children'].append(p2)
                    else:
                        hassame = 0
                        for tmp in p1['children']:
                            if tmp.get('id') == p2.get('id'):
                                hassame =1
                        if hassame == 0:
                            p1['children'].append(p2)
            if p0.get('id') == p1.get('parent_id'):
                if p0.get("children") is None:
                    p0['children'] = []
                p0['children'].append(p1)
        menu.append(p0)
    return menu


# 生成验证码
def get_captcha():
    code, image = gen_captcha()
    out = BytesIO()
    session["code"] = code
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp, code


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
        "collaspe": False,
        # 是否同时只打开一个菜单目录
        "accordion": True,
        "method": "GET",
        # 是否开启多系统菜单模式
        "control": False,
        # 顶部菜单宽度 PX
        "controlWidth": 500,
        # 默认选中的菜单项
        "select": "0",
        # 是否开启异步菜单，false 时 data 属性设置为菜单数据，false 时为 json 文件或后端接口
        "async": True
    }, tab={
        # 是否开启多选项卡
        "enable": True,
        # 切换选项卡时，是否刷新页面状态
        "keepState": True,
        # 是否开启 Tab 记忆
        "session": True,
        # 最大可打开的选项卡数量
        "max": 30,
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
