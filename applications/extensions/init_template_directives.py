from flask import session


def init_template_directives(app):
    @app.template_global()
    def authorize(power):
        return bool(power in session.get('permissions'))
