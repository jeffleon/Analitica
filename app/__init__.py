from config import config
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_jwt_extended import JWTManager

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in your code!
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    bootstrap.init_app(app)
    mail.init_app(app)
    jwt.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    from .main import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app