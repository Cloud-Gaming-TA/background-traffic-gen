# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

RUN apt-get update && \
    apt install -y iputils-ping

# Run app.py when the container launches
CMD ["python", "main.py", "192.168.1.1"]
