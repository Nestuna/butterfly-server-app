#  GNU nano 4.8                                                                               Dockerfile                                                                               Modifié  
# Pull a base image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a working directory for the django project
WORKDIR /code

# Copy requirements to the container
COPY Pipfile Pipfile.lock /code/

# Install the requirements to the container
RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev 
RUN apt-get install -y build-essential 
RUN pip install pipenv && pipenv install --system

# Copy the project files into the working directory
COPY . /code/

# Open a port on the container
EXPOSE 8000

