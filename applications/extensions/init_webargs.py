from marshmallow import EXCLUDE
from webargs.flaskparser import FlaskParser


class Parser(FlaskParser):
    DEFAULT_UNKNOWN_BY_LOCATION = {"query": EXCLUDE}


parser = Parser()