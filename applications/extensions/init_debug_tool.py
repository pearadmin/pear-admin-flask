from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


def init_debug_tool(app: Flask):
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)
