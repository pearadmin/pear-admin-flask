from datetime import datetime

from applications.extensions import db


class VipMember(db.Model):
    __tablename__ = 'vip_member'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='VIP用户ID')
    username = db.Column(db.String(20), comment='用户名')
    mobile = db.Column(db.String(11), comment='电话号码')
    id_card = db.Column(db.String(16), comment='身份证号码')
    wx = db.Column(db.String(50), comment='微信号')
    qq = db.Column(db.String(20), comment='QQ号')
    account = db.Column(db.String(50), comment='报名账号')
    number = db.Column(db.String(12), comment='学号')
    phase = db.Column(db.SMALLINT, comment='第几期')

    avatar = db.Column(db.String(255), comment='头像', default="/static/admin/admin/images/avatar.jpg")

    remark = db.Column(db.String(255), comment='备注')
    password_hash = db.Column(db.String(128), comment='哈希密码')
    enable = db.Column(db.Integer, default=0, comment='启用')

    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    courses = db.relationship('Course', secondary="vip_member_course", backref=db.backref('members'), lazy='dynamic')
    phases = db.relationship('Phase', secondary="vip_member_phase", backref=db.backref('members'), lazy='dynamic')


class Course(db.Model):
    __tablename__ = 'vip_course'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='课程id')
    name = db.Column(db.String(20), comment='课程名')


class Phase(db.Model):
    __tablename__ = 'vip_phase'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), comment='课程名')
    phase = db.Column(db.Integer, comment='第几期')
    teacher = db.Column(db.String(20), comment='带课讲师')


# 创建中间表
member_phase = db.Table(
    "vip_member_phase",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment='标识'),  # 主键
    db.Column("member_id", db.Integer, db.ForeignKey("vip_member.id"), comment='用户编号'),  # 属性 外键
    db.Column("phase_id", db.Integer, db.ForeignKey("vip_phase.id"), comment='期数编号'),  # 属性 外键
)

# 创建中间表
course_phase = db.Table(
    "vip_member_course",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment='标识'),  # 主键
    db.Column("member_id", db.Integer, db.ForeignKey("vip_member.id"), comment='用户编号'),  # 属性 外键
    db.Column("course_id", db.Integer, db.ForeignKey("vip_course.id"), comment='期数编号'),  # 属性 外键
)
