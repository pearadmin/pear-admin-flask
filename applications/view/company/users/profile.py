# 个人中心
from flask import render_template, request, make_response
from flask_login import login_required, current_user
from flask_restful import Resource
from applications.common.utils.http import fail_api, success_api
from applications.extensions import db
from applications.models import User
from applications.view.company.users import users_bp, user_api, user_curd


@users_bp.get('/center')
@login_required
def center():
    user_info = current_user
    user_logs = user_curd.get_current_user_logs()
    return render_template('admin/user/profile.html', user_info=user_info, user_logs=user_logs)


@user_api.resource('/avatar')
class Avatar(Resource):
    """修改头像"""

    def get(self):
        return make_response(render_template('admin/user/avatar.html'))

    def put(self):
        url = request.json.get("avatar").get("src")
        ret = User.query.filter_by(id=current_user.id).update({"avatar": url})
        db.session.commit()
        if not ret:
            return fail_api(msg="出错啦")
        return success_api(msg="修改成功")


# 修改当前用户信息
@users_bp.put('/updateInfo')
@login_required
def update_info():
    res_json = request.json
    if not user_curd.update_current_user_info(req_json=res_json):
        return fail_api(msg="出错啦")
    return success_api(msg="更新成功")


@user_api.resource('/editPassword')
class EditPassword(Resource):
    """前用户密码"""

    @login_required
    def get(self):
        return make_response(render_template('admin/user/edit_password.html'))

    @login_required
    def put(self):
        res_json = request.json
        return user_curd.edit_password(res_json=res_json)
