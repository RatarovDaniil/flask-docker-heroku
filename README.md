# flask-docker-heroku
It's a small guide about how to deploy flask app inside Docker container on Heroku.

### Install Docker localy:
1. ```sudo apt-get update```
2. ```sudo apt install docker.io```

### Enable Docker to run at startup:
1. ```sudo systemctl start docker```
2. ```sudo systemctl enable docker```

### Deploying existing application:
#### Login to Heroku container registry:
1. ```sudo heroku container:login```
#### From folder with Dockerfile run push your container to virtual server:
2. ```sudo heroku container:push web -a {name_of_your_heroku_app}```
#### Release your application:
3. ```heroku container:release web -a {name_of_your_heroku_app}```
#### Start virtual server on Heroku:
4. ```heroku ps:scale web=1 -a {name_of_your_heroku_app}```
