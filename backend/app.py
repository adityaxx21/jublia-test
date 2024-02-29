from app.tasks import celery_tasks
from celery import Celery

app = Celery('celery_tasks', broker='redis://localhost:6379/0')
if __name__ == '__main__':
    app.start()
