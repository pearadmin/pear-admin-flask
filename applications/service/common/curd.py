def model_to_dicts(Schema, model):
    # 如果是分页器返回，需要传入model.items
    common_schema = Schema(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = common_schema.dump(model)  # 生成可序列化对象
    return output
