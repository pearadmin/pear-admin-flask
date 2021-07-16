import os

import jinja2


class NewViewModular():

    def __init__(self, name):
        self.name = name

    def path_is_exists(self):
        return os.path.exists(f"applications/view/{self.name.split('/')[0]}")

    def new_dirs(self):
        if not self.path_is_exists():
            # 如果不存在则创建目录

            # 创建目录操作函数
            os.makedirs(f"applications/view/{self.name.split('/')[0]}")

            print(self.name + ' 创建成功')
            return True
        else:
            return False

    def add_view(self):
        # jinja渲染
        templateLoader = jinja2.FileSystemLoader(searchpath='applications/common/script/newmodular/template/')
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = "view"
        template = templateEnv.get_template(TEMPLATE_FILE, )
        templateVars = {"name": self.name}
        outputText = template.render(templateVars)
        with open(f"applications/view/{self.name}.py", "a", encoding='utf-8') as f:
            f.write(outputText)
            f.close()

    def add_init(self):
        # 判断__init__.py
        if os.path.exists(f"applications/view/{self.name.split('/')[0]}/__init__.py"):
            with open(f"applications/view/{self.name.split('/')[0]}/__init__.py", "r") as file:
                lines = file.readlines()
                print(lines)
                file.close()
                import_line_num = 0
                for line in lines:
                    if 'def' in line:
                        import_line_num = lines.index(line) - 2
            with open(f"applications/view/{self.name.split('/')[0]}/__init__.py", "w") as file:
                lines.insert(import_line_num,
                             f"from applications.view.{self.name.replace('/', '.')} import {self.name.replace('/', '_')}\n")
                print(lines)
                lines.insert(len(lines) - 1, f"    app.register_blueprint({self.name.replace('/', '_')})\n")
                print(lines)
                file.writelines(lines)
                file.close()
            return True
        else:
            templateLoader = jinja2.FileSystemLoader(searchpath='applications/common/script/newmodular/template/')
            templateEnv = jinja2.Environment(loader=templateLoader)
            TEMPLATE_FILE = "__init__"
            template = templateEnv.get_template(TEMPLATE_FILE, )
            templateVars = {"name": self.name}
            output = template.render(templateVars)
            with open(f"applications/view/{self.name.split('/')[0]}/__init__.py", "a", encoding='utf-8') as f:
                f.write(output)
                f.close()
            self.add_root_init()
            return True

    def add_root_init(self):
        with open(f"applications/view/__init__.py", "r") as file:
            lines = file.readlines()
            file.close()
            import_line_num = 0
            for line in lines:
                if 'def' in line:
                    import_line_num = lines.index(line) - 2
        with open(f"applications/view/__init__.py", "w") as file:
            lines.insert(
                import_line_num,
                f"from applications.view.{self.name.split('/')[0]} import register_{self.name.split('/')[0]}_views\n")
            print(lines)
            lines.insert(len(lines) - 1, f"    register_{self.name.split('/')[0]}_views(app)\n")
            print(lines)
            file.writelines(lines)
            file.close()

    def new_view(self):
        self.new_dirs()
        self.add_view()
        self.add_init()
