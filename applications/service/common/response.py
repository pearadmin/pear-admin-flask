from flask import jsonify

'''
成功响应

默认值”成功“

'''


def success_api(msg: str = "成功"):
    return jsonify(success=True, msg=msg)


'''

失败响应
默认值“失败”

'''


def fail_api(msg: str = "失败"):
    return jsonify(success=False, msg=msg)

'''

动态表格渲染响应

'''


def table_api(msg: str = "", count=0, data=None, limit=10):
    res = {
        'msg': msg,
        'code': 0,
        'data': data,
        'count': count,
        'limit': limit

    }
    return jsonify(res)
