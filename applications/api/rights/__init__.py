from flask_restful import Api

from .department import Departments, Department, DeptEnable
from .rights import RightRights, RightPower, RightPowerEnable, AdminConfigs, AdminMenu
from .roles import RoleRoles, RoleRole, RoleEnable, RolePower


def register_rights_api(api_bp):
    dept_api = Api(api_bp, prefix='/dept')
    dept_api.add_resource(Departments, '/departments')
    dept_api.add_resource(Department, '/department/<int:dept_id>')
    dept_api.add_resource(DeptEnable, '/department/<int:dept_id>/status')

    rights_api = Api(api_bp, prefix='/rights')
    rights_api.add_resource(RightRights, '/rights')
    rights_api.add_resource(RightPower, '/power/<int:power_id>')
    rights_api.add_resource(RightPowerEnable, '/power/<int:right_id>/status')
    rights_api.add_resource(AdminConfigs, '/configs')
    rights_api.add_resource(AdminMenu, '/menu')

    role_api = Api(api_bp, prefix='/roles')
    role_api.add_resource(RoleRoles, '/roles')
    role_api.add_resource(RoleRole, '/role/<int:role_id>')
    role_api.add_resource(RoleEnable, '/role/<int:role_id>/status')
    role_api.add_resource(RolePower, '/role_power/<int:role_id>')
