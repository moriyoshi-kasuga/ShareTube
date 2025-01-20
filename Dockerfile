# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.13

FROM python:${PYTHON_VERSION}-slim AS builder

WORKDIR /backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM builder AS dev

WORKDIR /backend

COPY . .

# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]

FROM builder AS prod

WORKDIR /backend

COPY . .

# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]
