# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.13

FROM python:${PYTHON_VERSION}-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

FROM builder AS dev

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]

FROM builder AS prod

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]
