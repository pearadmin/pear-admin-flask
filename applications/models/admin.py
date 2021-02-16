import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from applications.models import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    # 哈希密码
    password_hash = db.Column(db.String(128))
    # 启用
    status = db.Column(db.Integer, default=1)
    # 角色
    role = db.Column(db.Enum(
        '管理员', '普通用户', '游客'
    ), server_default='普通用户', nullable=False)
    # 创建时间
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)
    # 更新时间
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_authenticated(self):
        if self.status is 1:
            return True
        return False
