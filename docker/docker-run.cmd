@ECHO OFF

docker kill ubuntu-django
docker rm ubuntu-django
docker run --link mysql-misc -p 8000:8000 -v %~dp0\..\:/var/djangoproject --name ubuntu-django -d ubuntu-django:latest
