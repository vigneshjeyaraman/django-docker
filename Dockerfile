FROM python:3.8-alpine

# this is something needed when we run python on docker
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
# these are few dependencies that are required to install pycopg2 and postgres
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir app/
WORKDIR /app
COPY ./todo-project /app
