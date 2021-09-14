from flask_restful import Api

from .department import DepartmentsResource, DepartmentResource, DeptEnableResource
from .rights import (
    RightRightsResource, RightPowerResource, RightPowerEnableResource, AdminConfigsResource,
    AdminMenuResource
)
from .roles import RoleRolesResource, RoleRoleResource, RoleEnableResource, RolePowerResource


def register_rights_api(api_bp):
    dept_api = Api(api_bp, prefix='/dept')
    dept_api.add_resource(DepartmentsResource, '/departments')
    dept_api.add_resource(DepartmentResource, '/department/<int:dept_id>')
    dept_api.add_resource(DeptEnableResource, '/department/<int:dept_id>/status')

    rights_api = Api(api_bp, prefix='/rights')
    rights_api.add_resource(RightRightsResource, '/rights')
    rights_api.add_resource(RightPowerResource, '/power/<int:power_id>')
    rights_api.add_resource(RightPowerEnableResource, '/power/<int:right_id>/status')
    rights_api.add_resource(AdminConfigsResource, '/configs')
    rights_api.add_resource(AdminMenuResource, '/menu')

    role_api = Api(api_bp, prefix='/roles')
    role_api.add_resource(RoleRolesResource, '/roles')
    role_api.add_resource(RoleRoleResource, '/role/<int:role_id>')
    role_api.add_resource(RoleEnableResource, '/role/<int:role_id>/status')
    role_api.add_resource(RolePowerResource, '/role_power/<int:role_id>')
