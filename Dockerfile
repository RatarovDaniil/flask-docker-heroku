# grab the latest CentOS image
FROM ubuntu:latest

# metadata about maintainer
MAINTAINER Daniil Ratarov "daniil.ratarov@gmail.com"

# install python and pip
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# create dir for app
RUN mkdir /opt/flask_docker_app

# set up working directory
WORKDIR /opt/flask_docker_app

# copy all files from current folder to working directory
ADD . .

# install requirements
RUN pip3 install -r requirements.txt

# Expose is NOT supported by Heroku
# EXPOSE 5000

# Run the app. CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn -k gevent --bind 0.0.0.0:$PORT --worker-connections 100 app:app 

