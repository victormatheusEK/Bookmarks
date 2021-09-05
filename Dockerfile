FROM ubuntu:20.04
MAINTAINER "Victor Matheus"

RUN apt-get update -y && \
    apt install -y python3 pip

ENV TZ="America/Sao_Paulo"

COPY . /code
WORKDIR /code

RUN pip3 install -r requirements.txt && \
    python3 manage.py migrate