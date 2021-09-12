import typing as t


def success_api(message: str = "成功", code: int = 200) -> t.Dict:
    """ 成功响应 默认值”成功“ """
    return dict(success=True, message=message, code=code)


def fail_api(message: str = "失败", code: int = 404) -> t.Dict:
    """ 失败响应 默认值“失败” """
    return dict(success=False, message=message, code=code)


def table_api(success: bool = True,
              message: str = "",
              result: t.Union[dict, list] = None,
              code: int = 0) -> t.Dict:
    """
        动态表格渲染响应
        此方法返回数据给前端
        {
            'success': True,
            'code': 10002,
            'message': '提示消息',
            'result':{'items':[],'total': 100}
        }

        注：lay_ui 表格数据需要指定 code=0
    """
    ret = {
        'success': success,
        'message': message,
        'code': code,
        'result': result,
    }
    return ret
