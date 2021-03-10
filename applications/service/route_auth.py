from functools import wraps

from flask import abort, request, jsonify

from flask_login import current_user


def check_auth(authList: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.role in authList:
                if request.method == 'GET':
                    abort(403)
                else:
                    return jsonify(code=403, msg="权限不足!")
            return func(*args, **kwargs)

        return wrapper

    return decorator
