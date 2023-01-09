# base image  
FROM python:3.10
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME

RUN apt-get -y update
RUN apt-get -y upgrade

# run this command to install all dependencies  
RUN pip install -r r.txt  

RUN apt-get install -y sqlite3 libsqlite3-dev

COPY base.html /usr/local/lib/python3.10/site-packages/jazzmin/templates/admin/base.html
COPY index.html /usr/local/lib/python3.10/site-packages/jazzmin/templates/admin/index.html


VOLUME /workspaces /home/app/webapp/test
# port where the Django app runs  
EXPOSE 8000 
# start server  
CMD python manage.py runserver 0.0.0.0:8000 