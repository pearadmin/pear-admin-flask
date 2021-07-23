from flask import render_template

from applications.common.utils.rights import authorize
from applications.view import index_bp


@index_bp.get('/dept')
@authorize("admin:dept:main", log=True)
def dept_index():
    return render_template('department/main.html')
