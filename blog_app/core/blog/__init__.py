from flask import Blueprint

bp = Blueprint('blog', __name__)

from core.blog import routes