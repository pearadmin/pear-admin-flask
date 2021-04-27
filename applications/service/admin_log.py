from flask_login import current_user

from applications.models import db
from applications.models.admin_log import AdminLog


def login_log(request,uid, is_access):
    info = {
        'method': request.method,
        'url': request.path,
        'ip': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'desc': request.form.get('username'),
        'uid': uid,
        'success': int(is_access)

    }
    log = AdminLog(
        url=info.get('url'),
        ip=info.get('ip'),
        user_agent=info.get('user_agent'),
        desc=info.get('desc'),
        uid=info.get('uid'),
        method=info.get('method'),
        success = info.get('success')
    )
    db.session.add(log)
    db.session.flush()
    db.session.commit()
    return log.id


def admin_log(request, is_access):
    info = {
        'method': request.method,
        'url': request.path,
        'ip': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'desc': str(dict(request.values)),
        'uid': current_user.id,
        'success':int(is_access)

    }
    log = AdminLog(
        url=info.get('url'),
        ip=info.get('ip'),
        user_agent=info.get('user_agent'),
        desc=info.get('desc'),
        uid=info.get('uid'),
        method=info.get('method'),
        success=info.get('success')
    )
    db.session.add(log)
    db.session.commit()

    return log.id
