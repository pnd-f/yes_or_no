from flask import Flask
from app import include_views, include_other_views


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('./config.py', False)
    include_views(app)
    include_other_views(app)
    return app
