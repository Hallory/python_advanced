from flask import Flask
from app_runner import create_app
from app_runner import init_database, register_routers

app = Flask(__name__)

create_app(app)

init_database(app)

register_routers(app)
