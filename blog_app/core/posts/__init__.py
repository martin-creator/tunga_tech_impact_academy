from flask import Blueprint

bp = Blueprint('posts', __name__)

from core.posts import routes