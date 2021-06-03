from flask_debugtoolbar import DebugToolbarExtension


def open_debug_tool(app):
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)
