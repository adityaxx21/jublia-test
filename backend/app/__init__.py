import os

from flask import Flask
from model.models import db
from rest.mail_rest import api
from flask_mail import Mail
from celery import Celery, Task
mail = Mail()


def create_app(config_name="development"):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        CELERY=dict(
            broker_url="redis://localhost",
            result_backend="redis://localhost",
            task_ignore_result=True,
        ),
    )

    # Load configuration based on config_name
    if config_name == 'development':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/mailScheduller'
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
        app.config['MAIL_PORT'] = 2525
        app.config['MAIL_USERNAME'] = '965f1e27146fca'
        app.config['MAIL_PASSWORD'] = '05ff510932c3b5'
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False
        app.config['CELERY_BROKER_URL'] =  'redis://localhost:6379/0'
        app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/1'

    elif config_name == 'production':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/mailScheduller'
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Initialize SQLAlchemy

    db.init_app(app)
    mail.init_app(app)
    celery_app = celery_init_app(app)
    
    with app.app_context():
        db.create_all()
        app.register_blueprint(api)

    return app

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app
    
if __name__ == '__main__':
    app = create_app('development')
    app.run()