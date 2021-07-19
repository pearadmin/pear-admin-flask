import os
from flask import Blueprint, request, render_template, jsonify, current_app

from applications.common.utils.http import fail_api, success_api, table_api
from applications.common.utils.rights import authorize
from applications.extensions import db
from applications.models import Photo
from applications.common.utils import upload as upload_curd

admin_file = Blueprint('adminFile', __name__, url_prefix='/admin/file')


#  图片管理
@admin_file.get('/')
@authorize("admin:file:main", log=True)
def index():
    return render_template('admin/photo/photo.html')


#  图片数据
@admin_file.get('/table')
@authorize("admin:file:main", log=True)
def table():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    data, count = upload_curd.get_photo(page=page, limit=limit)
    return table_api(data=data, count=count)


#   上传
@admin_file.get('/upload')
@authorize("admin:file:add", log=True)
def upload():
    return render_template('admin/photo/photo_add.html')


#   上传接口
@admin_file.post('/upload')
@authorize("admin:file:add", log=True)
def upload_api():
    if 'file' in request.files:
        photo = request.files['file']
        mime = request.files['file'].content_type

        file_url = upload_curd.upload_one(photo=photo, mime=mime)
        res = {
            "msg": "上传成功",
            "code": 0,
            "success": True,
            "data":
                {"src": file_url}
        }
        return jsonify(res)
    return fail_api()


#    图片删除
@admin_file.route('/delete', methods=['GET', 'POST'])
@authorize("admin:file:delete", log=True)
def delete():
    _id = request.form.get('id')
    res = upload_curd.delete_photo_by_id(_id)
    if res:
        return success_api(msg="删除成功")
    else:
        return fail_api(msg="删除失败")


# 图片批量删除
@admin_file.route('/batchRemove', methods=['GET', 'POST'])
@authorize("admin:file:delete", log=True)
def batch_remove():
    ids = request.form.getlist('ids[]')
    photo_name = Photo.query.filter(Photo.id.in_(ids)).all()
    upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
    for p in photo_name:
        os.remove(upload_url + '/' + p.name)
    photo = Photo.query.filter(Photo.id.in_(ids)).delete(synchronize_session=False)
    db.session.commit()
    if photo:
        return success_api(msg="删除成功")
    else:
        return fail_api(msg="删除失败")
