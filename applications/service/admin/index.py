from io import BytesIO
from flask import session, make_response
from flask_login import current_user
from applications.models.admin_power import PowerSchema
from applications.service.CaptchaTool import gen_captcha


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
    role = current_user.role
    power0 = []
    power1 = []
    for i in role:
        if i.enable == 0:
            continue
        for p in i.power:
            if p.enable == 0:
                continue
            if int(p.type) == 0:
                power0.append(p)
            else:
                power1.append(p)

    power_schema = PowerSchema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    power0_dict = power_schema.dump(power0)  # 生成可序列化对象
    power1_dict = power_schema.dump(power1)  # 生成可序列化对象
    power0_dict = sorted(power0_dict, key=lambda i: i['sort'])
    power1_dict = sorted(power1_dict, key=lambda i: i['sort'])
    # print(power0)
    # print(power1)

    menu = []

    for p0 in power0_dict:
        for p1 in power1_dict:
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
