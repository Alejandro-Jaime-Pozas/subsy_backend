# name of the tag; py version 3.10, alpine is a linux based lightweight version of python
FROM python:3.10-alpine3.19
LABEL maintainer="https://portfolio-alejandro-jaime.web.app/"

# sets python unbuffered to true so that python logs are directly displayed when container is running
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user