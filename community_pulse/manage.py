from flask import Flask
from app_runner import create_app

def create_app_cli():
    app = Flask(__name__)
    create_app(app)
    return app
