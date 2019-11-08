FROM python:3.7-alpine
LABEL Gopal Yadav

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base
COPY ./requirements.txt /requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./ /app

RUN adduser -D user
USER user
