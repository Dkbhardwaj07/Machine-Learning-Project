FROM python:3.10
Copy . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --worker --bind 0.0.0.0:$PORT app:app
