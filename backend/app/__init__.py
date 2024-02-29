import os

from flask import Flask
from .utils import celery_init_app
from .models.models import db
from .api.mail_rest import api

from flask_mail import Mail
from celery import Celery, Task
mail = Mail()


def create_app(config_name="development"):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Load configuration based on config_name
    if config_name == 'development':
        app.config.from_mapping(
            SECRET_KEY='dev',
            CELERY=dict(
                broker_url="redis://localhost:6379/0",
                result_backend="redis://localhost:6379/1",
                task_ignore_result=True,
            ),
            SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/mailScheduller',
            DEBUG = True,
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            MAIL_SERVER = 'sandbox.smtp.mailtrap.io',
            MAIL_PORT = 2525,
            MAIL_USERNAME = '965f1e27146fca',
            MAIL_PASSWORD = '05ff510932c3b5',
            MAIL_USE_TLS = True,
            MAIL_USE_SSL = False,
            CELERY_BROKER_URL = 'redis://localhost:6379/0',
            CELERY_RESULT_BACKEND = 'redis://localhost:6379/1',
        )

    elif config_name == 'production':
        app.config.from_mapping(
            SECRET_KEY='dev',
            CELERY=dict(
                broker_url="",
                result_backend="",
                task_ignore_result=True,
            ),
            SQLALCHEMY_DATABASE_URI = '',
            DEBUG = False,
            SQLALCHEMY_TRACK_MODIFICATIONS = True,
            MAIL_SERVER = '',
            MAIL_PORT = '',
            MAIL_USERNAME = '',
            MAIL_PASSWORD = '',
            MAIL_USE_TLS = True,
            MAIL_USE_SSL = False,
            CELERY_BROKER_URL = '',
            CELERY_RESULT_BACKEND = '',
        )

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
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
        

    return app, celery

