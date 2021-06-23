from flask import Blueprint, render_template, make_response, Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import desc

from applications.common.utils.http import table_api
from applications.models import VipMember

vip_bp = Blueprint('vip', __name__, url_prefix='/vip')
vip_api = Api(vip_bp)


def register_vip_view(app: Flask):
    app.register_blueprint(vip_bp)


@vip_api.resource('/member')
class Member(Resource):
    def get(self):
        return make_response(render_template('admin/vip/main.html'))

    def post(self):
        pass


#   用户分页查询
@vip_bp.get('/data')
def data():
    parse = reqparse.RequestParser()
    parse.add_argument('page', type=int, default=1)
    parse.add_argument('limit', type=int, default=10)
    parse.add_argument('wx', type=str, default="")
    parse.add_argument('username', type=str, default="")

    res = parse.parse_args()

    filters = []
    if res.username:
        filters.append(VipMember.username.like('%{}%'.format(res.username)))

    if res.wx:
        filters.append(VipMember.wx.like('%{}%'.format(res.wx)))

    paginate = VipMember.query.filter(*filters).paginate(
        page=res.page, per_page=res.limit)

    return table_api(data=[
        {
            'id': item.id,
            'username': item.username,
            'mobile': item.mobile,
            'id_card': item.id_card,
            'wx': item.wx,
            'qq': item.qq,
            'account': item.account,
            'number': '{:0>2}{:0>4}'.format(item.phase, item.id),
            'create_at': item.update_at,
            'phase': item.phase,
        } for item in paginate.items], count=paginate.total)
