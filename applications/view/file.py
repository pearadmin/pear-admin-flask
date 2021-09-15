from flask import render_template

from applications.view import index_bp
from applications.common.utils.rights import view_logging_required, permission_required


@index_bp.get('/file')
@view_logging_required
@permission_required("admin:file:main")
def file_index():
    return render_template('admin/file/photo.html')


@index_bp.get('/file/photo/add')
@view_logging_required
@permission_required("admin:file:main")
def file_photo_add():
    return render_template('admin/file/photo_add.html')
