FROM python:3.10-slim-buster

WORKDIR /app

COPY pdm.lock pyproject.toml /app/

RUN pdm install

COPY ./core ./models ./repositories ./routers ./services ./main.py /app/

CMD pdm run dev