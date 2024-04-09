from flask.views import MethodView
import os
import requests
import redis
from rq import Queue
from blog_api.task import send_user_registration_email
from sqlalchemy import or_  # or_ is an "OR" operator for SQLAlchemy
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, get_jwt,jwt_required, create_refresh_token, get_jwt_identity
from blog_api.db import db
from blog_api.models import UserModel
from blog_api.schemas import UserSchema, UserRegisterSchema
from blog_api.blocklist import BLOCKLIST
# from blog_api.tasks import mail



blp = Blueprint("Users", __name__, description="Operations on users")

connection = redis.from_url(
    os.getenv("REDIS_URL")
)  # Get this from Render.com or run in Docker
queue = Queue("emails", connection=connection)



@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserRegisterSchema)
    def post(self, user_data):
        
        if UserModel.query.filter(or_(UserModel.username == user_data["username"],UserModel.email == user_data["email"])).first():
            abort(409, message="A user with that username or email already exists.")
            
        user = UserModel(
            username=user_data["username"],
            email=user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
       
        db.session.add(user)
        db.session.commit()

        queue.enqueue(send_user_registration_email, 'martinlubowa@outlook.com', 'martinlubowa')

        return {"message": "User created successfully."}, 201
    

@blp.route("/user/<int:user_id>")
class User(MethodView):
    """
    This resource can be useful when testing our Flask app.
    We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful
    when we are manipulating data regarding the users.
    """

    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}, 200
    

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password): # Fresh token and refresh token
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        abort(401, message="Invalid credentials.")


@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False) # Fresh token and refresh token
        # Make it clear that when to add the refresh token to the blocklist will depend on the app design
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"access_token": new_token}, 200




    