import yaml
import glob


def read_yaml(yaml_file_path):
    try:
        with open(yaml_file_path, 'rb') as f:
            cf = f.read()
    except FileNotFoundError:
        print('未找到配置文件')
    c = yaml.safe_load(cf)
    return c


def read_all_yaml(menu_yaml_path):
    lista = []
    lst = glob.glob(menu_yaml_path)
    for l in lst:
        a = read_yaml(l)
        lista.append(a)
    return lista
# zanshi_url = "D:\\it\\pear\\flask-admin-flask-simple\\applications\\views\\admin/../../config/menu\\*.yaml"
# a = read_all_yaml(zanshi_url)
# print(a)


def make_tree(menu_yaml_path,auth):
    a = read_all_yaml(menu_yaml_path)
    auth_tree= []

    for i in a:
        if auth in i.get('auth'):
            i_date = i.get('data')
            auth_tree.append(i_date)
    print(auth_tree)
    return auth_tree


# zanshi_url = "D:\\it\\pear\\flask-admin-flask-simple\\applications\\views\\admin/../../config/menu\\*.yaml"
# make_tree(zanshi_url,'管理员')

