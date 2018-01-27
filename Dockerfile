FROM tiangolo/uwsgi-nginx-flask:python2.7

ENV STATIC_INDEX 1

COPY ./app /app
