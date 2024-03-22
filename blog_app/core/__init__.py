from flask import Flask
from flask_migrate import Migrate
from core.main import bp as main_bp
from core.posts import bp as posts_bp
from core.questions import bp as question_bp
from core.blog import bp as blog_bp
from core.extensions import db
from core.auth import bp as auth_bp
from flask_login import LoginManager
from core.models.user import User

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

     # blueprint for auth routes in our app
    app.register_blueprint(auth_bp)

    # blueprint for non-auth parts of app
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    # Register blueprints here
    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp, url_prefix='/posts')
    app.register_blueprint(question_bp, url_prefix='/questions')
    app.register_blueprint(blog_bp, url_prefix='/blog')

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
