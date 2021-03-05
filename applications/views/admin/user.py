from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from flask_marshmallow import Marshmallow
from marshmallow import fields
from applications.models import db
from applications.models.admin import User
from applications.service.route_auth import check_auth
from applications.service.admin_log import  admin_log

admin_user = Blueprint('adminUser', __name__, url_prefix='/admin/user')
ma = Marshmallow()


@admin_user.before_request
@login_required
def Monitor_log():
    admin_log(request)


#                               ----------------------------------------------------------
#                               -------------------------  用户管理 --------------------------
#                               ----------------------------------------------------------


@admin_user.route('/')
@login_required
@check_auth(['管理员','普通用户','游客'])
def index():
    return render_template('admin/user.html')


#                               ==========================================================
#                                                            用户 分页查询
#                               ==========================================================


class UserSchema(ma.Schema):  # 序列化类
    id = fields.Integer()
    username = fields.Str()
    status = fields.Bool()
    role = fields.Str()
    create_at = fields.DateTime()
    update_at = fields.DateTime()


@admin_user.route('/table')
@login_required
@check_auth(['管理员','普通用户','游客'])
def table():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    user = User.query.paginate(page=page, per_page=limit, error_out=False)
    role_schema = UserSchema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = role_schema.dump(user.items)  # 生成可序列化对象
    res = {
        'msg': "",
        'code': 0,
        'data': output,
        'count': 1,
        'limit': "10"

    }
    return jsonify(res)


#                               ==========================================================
#                                                            用户增加
#                               ==========================================================


@admin_user.route('/insert', methods=['GET', 'POST'])
@login_required
@check_auth(['管理员'])
def insert():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        if username and password and role:
            if User.query.filter_by(username=username).first() is None:
                user = User(username=username, role=role)
                user.set_password(password)
                db.session.add(user)
                db.session.commit()

                res = {"msg": "添加成功", "code": 200}
                return jsonify(res)

            else:
                res = {"msg": "用户已经存在", "code": 999}
                return jsonify(res)
        else:
            res = {"msg": "用户名密码角色不能为空", "code": 999}
            return jsonify(res)


    else:
        role = ['管理员', '普通用户']
        return render_template('admin/user_add.html', role=role)


#                               ==========================================================
#                                                            删除用户
#                               ==========================================================


@admin_user.route('/delete', methods=['POST'])
@login_required
@check_auth(['管理员'])
def delete():
    id = request.form.get('id')
    user = User.query.filter_by(id=id).delete()
    db.session.commit()
    if user:
        res = {"msg": "删除成功", "code": 200}
        return jsonify(res)
    else:
        res = {"msg": "删除失败", "code": 999}
        return res


#                               ==========================================================
#                                                            编辑用户
#                               ==========================================================


@admin_user.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@check_auth(['管理员'])
def update(id):
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        if username and role:
            if password is None:
                if User.query.filter_by(id=id).first() is not None:
                    user = User.query.filter_by(id=id).update({'username': username, 'role': role})
                    db.session.commit()

                    res = {"msg": "修改成功", "code": 200}
                    return jsonify(res)

                else:
                    res = {"msg": "用户已经存在", "code": 200}
                    return jsonify(res)
            else:
                user = User.query.filter_by(id=id).first()
                if user is not None:
                    User.query.filter_by(id=id).update({'username': username, 'role': role})
                    user.set_password(password)
                    db.session.commit()

                    res = {"msg": "修改成功", "code": 200}
                    return jsonify(res)

                else:
                    res = {"msg": "用户不存在", "code": 200}
                    return jsonify(res)

        else:
            res = {"msg": "用户名密码角色不能为空", "code": 999, "test": str(username)}
            return jsonify(res)
    else:
        role = ['管理员', '普通用户']
        user = User.query.filter_by(id=id).first()
        return render_template('admin/user_edit.html', user=user, role=role)


#                               ==========================================================
#                                                            更新用户状态
#                               ==========================================================

@admin_user.route('/update/status', methods=['POST'])
@login_required
@check_auth(['管理员'])
def ustatus():
    id = request.form.get('id')
    status = request.form.get('status')
    if id and status:
        user = User.query.filter_by(id=id).update({'status': status})
        if user:
            db.session.commit()
        res = {"msg": "更新成功", "code": 200}
        return jsonify(res)
    return {"msg": "出错啦", "code": 999}


@admin_user.route('/batchRemove',methods=['GET','POST'])
@login_required
@check_auth(['管理员'])
def batchRemove():
    ids = request.form.getlist('ids[]')
    user = User.query.filter(User.id.in_(ids)).delete(synchronize_session=False)
    db.session.commit()
    if user:
        res = {"msg": "删除成功", "code": 200}
        return jsonify(res)
    else:
        res = {"msg": "删除失败", "code": 999}
        return res


