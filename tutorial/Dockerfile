FROM ubuntu:16.04
#installing ubuntu essentials
RUN apt-get update && apt-get -y install python3 python-dev python3-dev build-essential python3-pip libnuma-dev
RUN apt-get install -y python3-tk

# create directory
RUN mkdir /workdirectory

WORKDIR /workdirectory

ADD *.ipynb ./
ADD requirements.txt ./

RUN pip3 install -r requirements.txt 

RUN echo $'Run this command in the container to start: jupyter-notebook —-ip 0.0.0.0 —-no-browser —-allow-root'
RUN echo $'\nThen Go to http://localhost:8888/tree to view notebook!\n\n\n'