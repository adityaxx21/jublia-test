from app import create_app


app, celery = create_app('development')
  

if __name__ == "__main__":
    app.run()