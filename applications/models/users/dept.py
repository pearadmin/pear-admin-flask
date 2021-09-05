from applications.extensions import db
from ..base import BaseModel


class CompanyDepartment(db.Model, BaseModel):
    __tablename__ = 'cp_dept'
    id = db.Column(db.Integer, primary_key=True, comment="部门ID")
    parent_id = db.Column(db.Integer, comment="父级编号")
    dept_name = db.Column(db.String(50), comment="部门名称")
    sort = db.Column(db.Integer, comment="排序")
    leader = db.Column(db.String(50), comment="负责人")
    phone = db.Column(db.String(20), comment="联系方式")
    email = db.Column(db.String(50), comment="邮箱")
    status = db.Column(db.Integer, comment='状态(1开启,0关闭)')
    remark = db.Column(db.Text, comment="备注")
    address = db.Column(db.String(255), comment="详细地址")
