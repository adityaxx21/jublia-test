from app import create_app
from app.config import PORT
from celery.schedules import crontab

app, celery = create_app('development')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)