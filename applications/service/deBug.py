from flask_debugtoolbar import DebugToolbarExtension


def OpenDug(app):
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)
