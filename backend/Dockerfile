# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.10.12
FROM python:${PYTHON_VERSION}-slim as base

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variables
ENV BROKER_URL="redis://redis:6379/0"
ENV RESULT_BACKEND="redis://redis:6379/1"
ENV SQLALCHEMY_DATABASE_URI="postgresql://postgres:root@postgres/mailScheduller"
ENV SQLALCHEMY_TRACK_MODIFICATIONS=True
ENV MAIL_SERVER="sandbox.smtp.mailtrap.io"
ENV MAIL_PORT=2525
ENV MAIL_USERNAME="965f1e27146fca"
ENV MAIL_PASSWORD="05ff510932c3b5"
ENV MAIL_USE_TLS=True
ENV MAIL_USE_SSL=False
ENV MAIL_SENDER="jublia@example.com"

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]