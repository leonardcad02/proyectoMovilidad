from flask import Blueprints

auth = Blueprints('name', __name__, url_prefix = '/auth')

from . import auth