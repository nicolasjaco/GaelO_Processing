# base image  
FROM python:3.7.4 
# setup environment variable  
ENV DockerHOME=/home/gaelo_processing

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

COPY . $DockerHOME  
 
# install dependencies  
RUN pip install --upgrade pip
RUN pip install pipenv
# run this command to install all dependencies  
RUN pipenv install --system --deploy

EXPOSE 8000 
# start server
CMD python manage.py runserver 