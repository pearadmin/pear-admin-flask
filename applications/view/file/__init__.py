import os

from flask import Blueprint, request, render_template, current_app
from flask_restful import marshal
from sqlalchemy import desc

from applications.common.serialization import photo_fields
from applications.common.utils.http import table_api, success_api, fail_api
from applications.common.utils.rights import authorize
from applications.extensions import db
from applications.models import Photo

file_bp = Blueprint('file', __name__, url_prefix='/file')


#  图片管理
@file_bp.get('/')
@authorize("admin:file:main", log=True)
def index():
    return render_template('admin/file/photo.html')


#  图片数据
@file_bp.get('/table')
@authorize("admin:file:main", log=True)
def table():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    photo_paginate = Photo.query.order_by(desc(Photo.create_time)).paginate(page=page, per_page=limit, error_out=False)
    data = marshal(photo_paginate.items, photo_fields)
    return table_api(data=data, count=photo_paginate.total)


# 图片批量删除
@file_bp.route('/batchRemove', methods=['GET', 'POST'])
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


from . import file
