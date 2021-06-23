from applications.models.company import Dept, DeptSchema, User, UserSchema
from .dict_models import DictType, DictData, DictTypeSchema, DictDataSchema
from .log import AdminLog, LogSchema
from applications.models.file.photo import Photo, PhotoSchema
from applications.models.rights.power import Power, PowerSchema, PowerSchema2
from applications.models.rights.role import Role, RoleSchema
from applications.models.rights.role_power import role_power
from applications.models.rights.user_role import user_role
from applications.models.vip import VipMember, Course, Phase, course_phase, member_phase
