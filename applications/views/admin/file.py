import os

from flask import Blueprint, request, render_template, jsonify, current_app
from flask_login import login_required
from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy import desc

from applications.models import db
from applications.models.admin import Photo
from applications.service.route_auth import check_auth
from applications.service.upload import photos

ma = Marshmallow()
admin_file = Blueprint('adminFile', __name__, url_prefix='/admin/file')


@admin_file.route('/')
@login_required
@check_auth(['管理员','普通用户','游客'])
def index():
    return render_template('admin/photo.html')


class PhotoSchema(ma.Schema):  # 序列化类
    id = fields.Integer()
    name = fields.Str()
    href = fields.Str()
    mime = fields.Str()
    size = fields.Str()
    ext = fields.Str()
    create_time = fields.DateTime()


@admin_file.route('/table')
@login_required
@check_auth(['管理员','普通用户','游客'])
def table():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    photo = Photo.query.order_by(desc(Photo.create_time)).paginate(page=page, per_page=limit, error_out=False)
    count = Photo.query.count()
    role_schema = PhotoSchema(many=True)
    output = role_schema.dump(photo.items)
    res = {
        'msg': "",
        'code': 0,
        'data': output,
        'count': count,
        'limit': "10"

    }
    return jsonify(res)


@admin_file.route('/upload', methods=['GET', 'POST'])
@login_required
@check_auth(['管理员'])
def upload():
    if request.method == 'POST' and 'file' in request.files:
        filename = photos.save(request.files['file'])
        file_url = photos.url(filename)
        mime = request.files['file'].content_type
        upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
        size = os.path.getsize(upload_url + '/' + filename)
        photo = Photo(name=filename, href=file_url, mime=mime, size=size)
        db.session.add(photo)
        db.session.commit()
        res = {
            "msg": "上传成功",
            "code": 0,
            "data":
                {"src": file_url}
        }
        return jsonify(res)

    return render_template('admin/photo_add.html')


@admin_file.route('/delete', methods=['GET', 'POST'])
@login_required
@check_auth(['管理员'])
def delete():
    id = request.form.get('id')
    photo_name = Photo.query.filter_by(id=id).first().name
    photo = Photo.query.filter_by(id=id).delete()
    db.session.commit()
    upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
    os.remove(upload_url + '/' + photo_name)
    if photo:
        res = {"msg": "删除成功", "code": 200}
        return jsonify(res)
    else:
        res = {"msg": "删除失败", "code": 999}
        return res


@admin_file.route('/batchRemove', methods=['GET', 'POST'])
@login_required
@check_auth(['管理员'])
def batchRemove():
    ids = request.form.getlist('ids[]')
    photo_name = Photo.query.filter(Photo.id.in_(ids)).all()
    upload_url = current_app.config.get("UPLOADED_PHOTOS_DEST")
    photo_list = []
    for p in photo_name:
        os.remove(upload_url + '/' + p.name)
    photo = Photo.query.filter(Photo.id.in_(ids)).delete(synchronize_session=False)
    db.session.commit()
    if photo:
        res = {"msg": "删除成功", "code": 200}
        return jsonify(res)
    else:
        res = {"msg": "删除失败", "code": 999}
        return res
