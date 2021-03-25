from flask import session


def init_template_global(app):
    @app.template_global()
    def authorize(power):
        # print(power)
        # print(session.get('permissions'))
        return bool(power in  session.get('permissions'))


