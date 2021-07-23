from flask import render_template

from applications.view import index_bp
from applications.common.utils.rights import authorize


#  图片管理
@index_bp.get('/file')
@authorize("admin:file:main", log=True)
def file_index():
    return render_template('file/photo.html')
