from flask import render_template

from applications.common.utils.rights import authorize
from applications.models import RightsPower
from applications.view import index_bp


@index_bp.get('/rights/')
@authorize("admin:power:main", log=True)
def rights_index():
    return render_template('admin/rights/rights.html')


@index_bp.get('/rights/power/<int:power_id>')
@authorize("admin:power:edit", log=True)
def rights_edit(power_id):
    power = RightsPower.query.filter_by(id=power_id).first()
    icon = str(power.icon).split()
    if len(icon) == 2:
        icon = icon[1]
    else:
        icon = None
    return render_template('admin/rights/rights_edit.html', power=power, icon=icon)


@index_bp.get('/rights/add')
@authorize("admin:power:main", log=True)
def rights_add():
    return render_template('admin/rights/rights_add.html')
