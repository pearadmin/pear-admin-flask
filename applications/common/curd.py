from applications.extensions import db, ma


def model_to_dicts(schema: ma.Schema, data):
    """
    :param schema: schema类
    :param model: sqlalchemy查询结果
    :return: 返回单个查询结果
    """
    # 如果是分页器返回，需要传入model.items
    common_schema = schema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = common_schema.dump(data)  # 生成可序列化对象
    return output


def get_one_by_id(model: db.Model, id):
    """
    :param model: 模型类
    :param id: id
    :return: 返回单个查询结果
    """
    return model.query.filter_by(id=id).first()


def delete_one_by_id(model: db.Model, id):
    """
    :param model: 模型类
    :param id: id
    :return: 返回单个查询结果
    """
    r = model.query.filter_by(id=id).delete()
    db.session.commit()
    return r


# 启动状态
def enable_status(model: db.Model, id):
    enable = 1
    role = model.query.filter_by(id=id).update({"enable": enable})
    if role:
        db.session.commit()
        return True
    return False


# 停用状态
def disable_status(model: db.Model, id):
    enable = 0
    role = model.query.filter_by(id=id).update({"enable": enable})
    if role:
        db.session.commit()
        return True
    return False
