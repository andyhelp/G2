#!/bin/sh

SOCKET=/tmp/user-socket-$USER.fastcgi
PIDFILE=/tmp/${USER}django.pid

#Change the values below to fit your memory and performance requirements
#The values below are for the lowest possible memory usage I was able to get
MAX_REQUESTS=5
MAX_CHILDRENS=1
MAX_SPARE=2

echo "python manage.py runfcgi maxrequests=$MAX_REQUESTS maxchildren=$MAX_CHILDRENS maxspare=$MAX_SPARE method=prefork socket=$SOCKET pidfile=$PIDFILE umask=000"
python manage.py runfcgi maxrequests=$MAX_REQUESTS maxchildren=$MAX_CHILDRENS maxspare=$MAX_SPARE method=prefork socket=$SOCKET pidfile=$PIDFILE umask=000 

