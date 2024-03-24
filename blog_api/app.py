from flask import Flask



def create_app(config_class=None):
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Hello, World!'

    return app


