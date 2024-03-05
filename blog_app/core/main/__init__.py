from flask import Blueprint

bp = Blueprint('main', __name__)

from core.main import routes