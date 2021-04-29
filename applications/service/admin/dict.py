# 字典管理
# 查询字典类型


from applications.models import db
from applications.models.admin_dict import DictType, DictData, DictTypeSchema, DictDataSchema


# 通过type_code获取字典dict
# 例：get_dict('user_sex')
# [{'key': '男', 'value': 'boy'}, {'key': '女', 'value': 'girl'}]
from applications.service.common.curd import model_to_dicts


def get_dict(typecode: str):
    Dict_list = []
    if DictType.query.filter_by(type_code=typecode, enable=1).first():
        Dicts = DictData.query.filter_by(type_code=typecode, enable=1).all()
        for d in Dicts:
            Dict_Dict = {"key": d.data_label, "value": d.data_value}
            Dict_list.append(Dict_Dict)
    else:
        return None
    return Dict_list


def get_dict_type(page, limit, type_name):
    dict_all = DictType.query
    if type_name:
        dict_all = dict_all.filter(DictType.type_name.like('%' + type_name + '%'))
    dict_all = dict_all.paginate(page=page,
                                 per_page=limit,
                                 error_out=False)
    count = DictType.query.count()
    data = model_to_dicts(Schema=DictTypeSchema,model=dict_all.items)
    return data, count


def get_dict_data(page, limit, type_code):
    dict_all = DictData.query.filter_by(type_code=type_code).paginate(page=page,
                                                                      per_page=limit,
                                                                      error_out=False)
    count = DictType.query.count()
    dict_dict = model_to_dicts(Schema=DictDataSchema,model=dict_all.items)
    return dict_dict, count


# 增加dicttype
def save_dict_type(req_json):
    description = req_json.get("description")
    enable = req_json.get("enable")
    type_code = req_json.get("typeCode")
    type_name = req_json.get("typeName")
    d = DictType(type_name=type_name, type_code=type_code, enable=enable, description=description)
    db.session.add(d)
    db.session.commit()
    return d.id


# 编辑字典类型
def update_dict_type(req_json):
    id = req_json.get("id")
    description = req_json.get("description")
    enable = req_json.get("enable")
    type_code = req_json.get("typeCode")
    type_name = req_json.get("typeName")
    DictType.query.filter_by(id=id).update({
        "description": description,
        "enable": enable,
        "type_code": type_code,
        "type_name": type_name
    })
    db.session.commit()
    return


def enable_dict_type_status(id):
    enable = 1
    res = DictType.query.filter_by(id=id).update({"enable": enable})
    if res:
        db.session.commit()
        return True
    return False


def disable_dict_type_status(id):
    enable = 0
    res = DictType.query.filter_by(id=id).update({"enable": enable})
    if res:
        db.session.commit()
        return True
    return False


# 删除字典类型
def delete_type_by_id(id):
    type_code = DictType.query.filter_by(id=id).first().type_code
    DictData.query.filter_by(type_code=type_code).delete()
    res = DictType.query.filter_by(id=id).delete()
    db.session.commit()
    return res


# 增加dictdata
def save_dict_data(req_json):
    data_label = req_json.get("dataLabel")
    data_value = req_json.get("dataValue")
    enable = req_json.get("enable")
    remark = req_json.get("remark")
    type_code = req_json.get("typeCode")
    d = DictData(data_label=data_label, data_value=data_value, enable=enable, remark=remark, type_code=type_code)
    db.session.add(d)
    db.session.commit()
    return d.id


# 编辑字典数据
def update_dict_data(req_json):
    id = req_json.get("dataId")
    DictData.query.filter_by(id=id).update({
        "data_label": req_json.get("dataLabel"),
        "data_value": req_json.get("dataValue"),
        "enable": req_json.get("enable"),
        "remark": req_json.get("remark"),
        "type_code": req_json.get("typeCode")
    })
    db.session.commit()
    return


def enable_dict_data_status(id):
    enable = 1
    res = DictData.query.filter_by(id=id).update({"enable": enable})
    if res:
        db.session.commit()
        return True
    return False


def disable_dict_data_status(id):
    enable = 0
    res = DictData.query.filter_by(id=id).update({"enable": enable})
    if res:
        db.session.commit()
        return True
    return False


# 删除dictdata
def delete_data_by_id(id):
    res = DictData.query.filter_by(id=id).delete()
    db.session.commit()
    return res
