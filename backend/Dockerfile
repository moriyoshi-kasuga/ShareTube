FROM python:3.13-slim

WORKDIR /backend

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]
