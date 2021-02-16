from functools import wraps

from flask import abort

from flask_login import current_user


def check_auth(authList: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.role in authList:
                abort(403)

            rs = func(*args, **kwargs)
            return rs

        return wrapper

    return decorator
