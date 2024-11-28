FROM python:3.13-slim
LABEL maintainer="Luke Tainton <luke@tainton.uk>"
LABEL org.opencontainers.image.source="https://github.com/luketainton/webexmemebot"
USER root

ENV PYTHONPATH="/run:/usr/local/lib/python3.13/lib-dynload:/usr/local/lib/python3.13/site-packages:/usr/local/lib/python3.13"
WORKDIR /run

COPY imp.py /run/imp.py

RUN mkdir -p /.local && \
    chmod -R 777 /.local && \
    pip install -U pip poetry

COPY pyproject.toml /run/pyproject.toml
COPY poetry.lock /run/poetry.lock

RUN poetry config virtualenvs.create false && \
    poetry install --without dev

ENTRYPOINT ["python3", "-B", "-m", "app.main"]

ARG version="dev"
ENV APP_VERSION=$version

COPY app /run/app
