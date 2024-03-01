import os

from flask import Flask
from .utils import celery_init_app, celery_sceduler
from .models.models import db
from .api.rest import api
from .config import config_by_name
from flask_cors import CORS

from flask_mail import Mail
mail = Mail()


def create_app(config_name="development"):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    
    # Load configuration based on config_name
    app.config.from_object(config_by_name[config_name])
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    mail.init_app(app)
    app.register_blueprint(api)
    app.config.from_prefixed_env()
    celery = celery_init_app(app)
    celery.set_default()
    celery_sceduler(celery)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
        

    return app, celery

