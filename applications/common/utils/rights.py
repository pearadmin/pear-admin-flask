import typing as t
from functools import wraps

from flask import abort, request, jsonify, session
from flask_login import login_required
from flask_login import current_user

from applications.extensions import db
from applications.models import LoggingModel


def record_logging(success: bool = True) -> None:
    """
    记录用户日志数据
    """
    info = {
        'method': request.method,
        'url': request.path,
        'ip': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'desc': str(dict(request.values)),
        'uid': current_user.id,
        'success': success
    }
    log = LoggingModel()
    for key, value in info.items():
        setattr(log, key, value)

    db.session.add(log)
    db.session.commit()


def view_logging_required(func: t.Callable) -> t.Callable:
    """
    日志装饰器，用于记录请求
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> t.Callable:
        record_logging()
        return func(*args, **kwargs)

    return wrapper


def permission_required(permission: str) -> t.Callable:
    """
    权限装饰器，用于过滤需要的权限
    """

    def decorator(func: t.Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> t.Callable:
            if permission not in session.get('permissions'):
                record_logging(success=False)
                abort(403)
            return func(*args, **kwargs)

        return wrapper

    return decorator
