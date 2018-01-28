FROM ubuntu:latest

# Prepare Framework
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install libmysqlclient-dev -y
RUN apt-get install git -y

RUN pip3 install --upgrade pip
RUN pip3 install Django
RUN pip3 install mysqlclient

# Prepare Workspace
# COMMENT NEXT 5 LINES AFTER FIRST RUN OF CONTAINER
#WORKDIR /tmp
#RUN django-admin startproject djangoproject
#WORKDIR /tmp/djangoproject
#RUN python3 manage.py migrate auth
#RUN python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'mea@mea.aws', 'superpass0')"


# Configure docker excecution
EXPOSE 8000

COPY entrypoint.sh /
ENTRYPOINT sh /entrypoint.sh
