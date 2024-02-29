from app import create_app
from celery.schedules import crontab

app, celery = create_app('development')
  
celery.conf.beat_schedule = {
    'add-every-60-seconds': {
        'task': 'app.tasks.celery_tasks.periodic_task',
        'schedule': 60.0,
    },
}
  
if __name__ == "__main__":
    app.run(debug=True)