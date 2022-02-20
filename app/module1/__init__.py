from flask import Blueprint

module1 = Blueprint('module1', __name__)
from . import views
