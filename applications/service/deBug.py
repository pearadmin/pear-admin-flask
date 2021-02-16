from flask_debugtoolbar import DebugToolbarExtension


def OpenDug(app):
    app.debug = True
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)
