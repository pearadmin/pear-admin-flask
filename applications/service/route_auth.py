from functools import wraps
from flask import abort, request, jsonify, session
from flask_login import login_required
from applications.service.admin_log import admin_log


def authorize(power: str):
    def decorator(func):
        @login_required
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not power in session.get('permissions'):
                if request.method == 'GET':
                    abort(403)
                else:
                    return jsonify(success=False, msg="权限不足!")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def authorize_and_log(power: str):
    def decorator(func):
        @login_required
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not power in session['permissions']:
                admin_log(request=request, is_access=False)
                if request.method == 'GET':
                    abort(403)
                else:
                    return jsonify(success=False, msg="权限不足!")
            admin_log(request=request, is_access=True)
            return func(*args, **kwargs)

        return wrapper

    return decorator
