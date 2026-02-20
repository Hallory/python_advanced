from flask import Flask
from config import settings
from app.extensions import db, migrate
from app.routers import questions

def create_app():
    flask_app = Flask(__name__)
    flask_app.config.update(settings.get_flask_config())

    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    import app.models  
    flask_app.register_blueprint(questions.questions_bp)

    return flask_app