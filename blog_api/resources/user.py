from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import UserSchema


blp = Blueprint("Users", "users", description="Operations on users")