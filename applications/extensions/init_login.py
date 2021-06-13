from flask_login import LoginManager


def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.login_view = 'passport.login'
    login_manager.login_message = u'请登录以访问此页面'

    @login_manager.user_loader
    def load_user(user_id):
        from applications.models import User
        user = User.query.get(int(user_id))
        return user
