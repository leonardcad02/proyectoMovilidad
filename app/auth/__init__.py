from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix = '/auth')

#vista
from . import views