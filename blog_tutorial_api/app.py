from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify
from blog_api.db import db
from flask_migrate import Migrate
import os
# from flask_mail import Mail, Message
from dotenv import load_dotenv
from blog_api.blocklist import BLOCKLIST
from blog_api.resources.user import blp as UserBlueprint
from blog_api.resources.item import blp as ItemBlueprint
from blog_api.resources.store import blp as StoreBlueprint
from blog_api.resources.tag import blp as TagBlueprint
# from blog_api.tasks_queues.task import init_mail

basedir = os.path.abspath(os.path.dirname(__file__))

# mail = Mail()

def create_app(db_url=None):
    
    app = Flask(__name__)
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "BLOP-REST-API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_REDOC_PATH"] = "/redoc"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    # app.config["SQLALCHEMY_DATABASE_URI"] =  "sqlite:///apis.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "tunga-impact-academy-2024"
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
    
    # # mail = Mail(app)
    # init_mail(app)
    # mail.init_app(app)

    jwt = JWTManager(app)

    db.init_app(app)
    migrate = Migrate(app, db)

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "tunga-impact-academy-2024" # Use str(secrets.SystemRandom().getrandbits(128)) to generate a random secret key
    jwt = JWTManager(app)
    

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )
    
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST


    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )
    
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )
    
    

    # with app.app_context():
    #     try:
    #         db.create_all()
    #         print("Database created successfully!")
    #     except Exception as e:
    #         print("Error creating database:", str(e))

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)


    return app





# app = create_app()
# api = Api(app)



# init_mail(app)

# api.register_blueprint(UserBlueprint)
# api.register_blueprint(ItemBlueprint)
# api.register_blueprint(StoreBlueprint)
# api.register_blueprint(TagBlueprint)



