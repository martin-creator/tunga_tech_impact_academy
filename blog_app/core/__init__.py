from flask import Flask
from core.main import bp as main_bp
from core.posts import bp as posts_bp
from core.questions import bp as question_bp
from core.extensions import db
from core.auth import bp as auth_bp

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

     # blueprint for auth routes in our app
    app.register_blueprint(auth_bp)

    # blueprint for non-auth parts of app
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    # Register blueprints here
    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp, url_prefix='/posts')
    app.register_blueprint(question_bp, url_prefix='/questions')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
