from config import config
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flasgger import Swagger
import os

SWAGGER_TEMPLATE = {"securityDefinitions": {"APIKeyHeader": {"type": "apiKey", "name": "Autorization", "in": "header"}}}
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
jwt = JWTManager()
swagger = Swagger(template=SWAGGER_TEMPLATE)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #load .env file
    load_dotenv()
    # configuration for a JWT 
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_SECRET_KEY"] = os.environ.get("SECRET_JWT")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    jwt.init_app(app)
    # bootstrap
    bootstrap.init_app(app)
    # mail
    mail.init_app(app)
    # dates manipulation
    moment.init_app(app)
    # add database
    db.init_app(app)
    # add Swagger to app 
    swagger.init_app(app)
    # add blueprints
    from .main import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app