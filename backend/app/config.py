from os import environ 
from dotenv import load_dotenv

load_dotenv('.env')

class DevelopmentConfig():
    SECRET_KEY='dev'
    CELERY=dict(
        broker_url="redis://localhost:6379/0",
        result_backend="redis://localhost:6379/1",
        task_ignore_result=True
    )
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/mailScheduller'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    
class ProductionConfig():
    SECRET_KEY='prod'
    CELERY=dict(
        broker_url = environ.get('BROKER_URL'),
        result_backend = environ.get('RESULT_BACKEND'),
        task_ignore_result=True
    )
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = environ.get('MAIL_PORT')
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = environ.get('MAIL_USE_SSL')
    
mail_sender = environ.get('MAIL_SENDER', 'jublia@example.com')

config_by_name = dict(
    development = DevelopmentConfig,
    production = ProductionConfig
)