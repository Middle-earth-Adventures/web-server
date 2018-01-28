#mv -v /tmp/djangoproject /var/djangoproject	# REMOVE AFTER FIRST RUN OF CONTAINER
python3 /var/djangoproject/djangoproject/manage.py migrate
python3 /var/djangoproject/djangoproject/manage.py runserver 0:8000