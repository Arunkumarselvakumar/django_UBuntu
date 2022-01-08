FROM ubuntu:20.04
USER root
RUN apt update && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update && apt upgrade -y
RUN apt install python3.8 python3-pip -y
RUN mkdir /backend
WORKDIR /backend
COPY . /backend/
RUN python3 -m pip install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
# ENTRYPOINT ["sh","/backend/run.sh"]