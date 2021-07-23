from flask import jsonify

"""
{
    'success': True,
    'code': 10002,
    'msg': '提示消息',
    'data':[] or {}
}
"""


def success_api(msg: str = "成功", code=200):
    """ 成功响应 默认值”成功“ """
    return jsonify(success=True, msg=msg, code=200)


def fail_api(msg: str = "失败", code=404):
    """ 失败响应 默认值“失败” """
    return jsonify(success=False, msg=msg, code=404)


def table_api(msg: str = "", count=0, data=None, limit=10, code=200):
    """ 动态表格渲染响应 """
    res = {
        'msg': msg,
        'code': code,
        'data': data,
        'count': count,
        'limit': limit
    }
    return jsonify(res)
