from celery import Celery
from celery.schedules import schedule

def celery_init_app(app):
    celery = Celery(app.import_name)
    celery.conf.update(app.config["CELERY"])

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

def celery_sceduler(celery):
    celery.conf.beat_schedule = {
        'add-every-60-seconds': {
            'task': 'app.tasks.celery_tasks.periodic_task',
            'schedule': 60.0,
        },
    }
    