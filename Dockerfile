FROM python:3.13-slim
LABEL maintainer="Luke Tainton <luke@tainton.uk>"
LABEL org.opencontainers.image.source="https://github.com/luketainton/webexmemebot"
USER root

ENV PYTHONPATH="/run:/usr/local/lib/python3.11/lib-dynload:/usr/local/lib/python3.11/site-packages:/usr/local/lib/python3.11"
WORKDIR /run

RUN mkdir -p /.local && \
    chmod -R 777 /.local && \
    pip install -U pip

COPY requirements.txt /run/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "-B", "-m", "app.main"]

ARG version="dev"
ENV APP_VERSION=$version

COPY app /run/app
