from app import create_app
from celery.schedules import crontab

app, celery = create_app('development')


if __name__ == "__main__":
    app.run(debug=True)