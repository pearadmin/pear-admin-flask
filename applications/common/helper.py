from sqlalchemy import and_

from applications.extensions import db


class ModelFilter:
    """
    orm多参数构造器
    """
    filter_field = {}
    filter_list = []

    type_exact = "exact"
    type_vague = "vague"

    def __init__(self):
        self.filter_field = {}
        self.filter_list = []

    def exact(self, field_name, value):
        """
        准确查询字段
        :param field_name: 模型字段名称
        :param value: 值
        """
        if value and value != '':
            self.filter_field[field_name] = {"data": value, "type": self.type_exact}

    def vague(self, field_name, value: str):
        """
        模糊查询字段
        :param field_name: 模型字段名称
        :param value: 值
        """
        if value and value != '':
            self.filter_field[field_name] = {"data": ('%' + value + '%'), "type": self.type_vague}

    def get_filter(self, model: db.Model):
        """
        获取过滤条件
        :param model: 模型字段名称
        """
        for k, v in self.filter_field.items():
            if v.get("type") == self.type_vague:
                self.filter_list.append(getattr(model, k).like(v.get("data")))
            if v.get("type") == self.type_exact:
                self.filter_list.append(getattr(model, k) == v.get("data"))
        return and_(*self.filter_list)
