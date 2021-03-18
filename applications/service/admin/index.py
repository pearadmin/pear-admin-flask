from io import BytesIO
from flask import session, make_response
from flask_login import current_user
from flask_marshmallow import Marshmallow
from marshmallow import fields
from applications.models.admin import Power
from applications.service.CaptchaTool import gen_captcha

ma = Marshmallow()


# 权限models序列化类
class PowerSchema(ma.Schema):
    id = fields.Integer()
    title = fields.Str(attribute="name")
    type = fields.Str()
    code = fields.Str()
    href = fields.Str(attribute="url")
    open_type = fields.Str()
    parent_id = fields.Integer()
    icon = fields.Str()
    sort = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()
    enable = fields.Integer()


# 授权路由存入session
def add_auth_session():
    role = current_user.role
    user_power = []
    for i in role:
        for y in i.power:
            user_power.append(y.code)
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
        for y in i.power:
            if int(y.type) == 0:
                power0.append(y)
            else:
                power1.append(y)

    power_schema = PowerSchema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    power0_dict = power_schema.dump(power0)  # 生成可序列化对象
    power1_dict = power_schema.dump(power1)  # 生成可序列化对象
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
