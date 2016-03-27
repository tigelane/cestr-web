FROM ubuntu:latest

MAINTAINER Tige Phillips <tige@tigelane.com>
# This container runs the web layer of CESTR
# CESTR is a very simple blog tool for demonstrating
# a three tier application

# Port to access the Flask application on - change if needed.
EXPOSE 80

RUN apt-get update
RUN apt-get -y upgrade

#################
# GIT                       #
#################
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install git

####################
# PYTHON and TOOLS #
####################
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python2.7 python-pip python-dev libmysqlclient-dev
RUN DEBIAN_FRONTEND=noninteractive pip install flask feedparser

#################
# cestr install #
#################
ADD cestr_web.py /opt/
ADD menu_items.py /opt/

# By default when this container runs, simply start the application
CMD /opt/cestr_web.py -D FOREGROUND
