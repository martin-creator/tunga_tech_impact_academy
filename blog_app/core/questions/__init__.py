from flask import Blueprint

bp = Blueprint('questions', __name__)

from core.questions import routes