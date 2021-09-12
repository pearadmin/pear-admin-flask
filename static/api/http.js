class File {
  constructor () {
    this.FILE_PATH = '/api/v1/file'
    this.FILE_API = {
      'PHOTOS': () => `${this.FILE_PATH}/photos`,
      'PHOTO': (photo_id) => `${this.FILE_PATH}/photo/${photo_id}`,
    }
  }
}

class Department {
  constructor () {
    this.DEPARTMENT_PATH = '/api/v1/dept'
    this.DEPARTMENT_API = {
      'DEPARTMENTS': () => `${this.DEPARTMENT_PATH}/departments`,
      'DEPARTMENT': (dept_id) => `${this.DEPARTMENT_PATH}/department/${dept_id}`,
      'DEPARTMENT_STATUS': (dept_id) => `${this.DEPARTMENT_PATH}/department/${dept_id}/status`,
    }
  }
}

class Rights {
  constructor () {
    this.DEPARTMENT_PATH = '/api/v1/rights'
    this.RIGHTS_API = {
      'RIGHTS': () => `${this.DEPARTMENT_PATH}/rights`,
      'POWER': (power_id) => `${this.DEPARTMENT_PATH}/power/${power_id}`,
      'POWER_STATUS': (power_id) => `${this.DEPARTMENT_PATH}/power/${power_id}/status`,
    }
  }
}

class Role {
  constructor () {
    this.ROLE_PATH = '/api/v1/roles'
    this.ROLE_API = {
      'ROLES': () => `${this.ROLE_PATH}/roles`,
      'ROLE': (role_id) => `${this.ROLE_PATH}/role/${role_id}`,
      'ROLE_STATUS': (role_id) => `${this.ROLE_PATH}/role/${role_id}/status`,
      'ROLE_POWER': (role_id) => `${this.ROLE_PATH}/role_power/${role_id}`,
    }
  }

  async get_roles () {
    return fetch(this.ROLE_API.ROLES()).then(function (response) {
      return response.json()
    }).then(function (myJson) {
      return myJson
    })
  }
}

class Users {
  constructor () {
    this.USER_PATH = '/api/v1/users'
    this.USER_API = {
      'USERS': () => `${this.USER_PATH}/users`,
      'USER': (user_id) => `${this.USER_PATH}/user/${user_id}`,
      'USER_ROLE': (user_id) => `${this.USER_PATH}/user/${user_id}/role`,
      'USER_STATUS': (user_id) => `${this.USER_PATH}/user/${user_id}/status`,
      'USER_AVATAR': (user_id) => `${this.USER_PATH}/user/${user_id}/avatar`,
      'USER_INFO': (user_id) => `${this.USER_PATH}/user/${user_id}/info`,
      'USER_PASSWORD': (user_id) => `${this.USER_PATH}/user/${user_id}/password`,
    }
  }

}

const FILE = new File()
const FILE_API = FILE.FILE_API
const DEPARTMENT = new Department()
const DEPARTMENT_API = DEPARTMENT.DEPARTMENT_API
const RIGHTS = new Rights()
const RIGHTS_API = RIGHTS.RIGHTS_API
const ROLE = new Role()
const ROLE_API = ROLE.ROLE_API
const USER = new Users()
const USER_API = USER.USER_API
export {
  FILE, FILE_API, DEPARTMENT,
  DEPARTMENT_API,
  RIGHTS, RIGHTS_API,
  ROLE, ROLE_API,
  USER, USER_API,
}

/******************数据解析********************************/
export function parserTableData (res) { //res 即为原始返回的数据
  console.log('parserTableData', res)
  return {
    'code': res.code, //解析接口状态
    'msg': res.message, //解析提示文本
    'count': res.result.total, //解析数据长度
    'data': res.result.items, //解析数据列表
  }
}