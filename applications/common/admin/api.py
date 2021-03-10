from flask import jsonify


def jsonApi(msg, code=200):
    res = {
        'msg': msg,
        'code': code
    }
    return jsonify(res)
