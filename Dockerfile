FROM python:3.6
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD gunicorn -b 0.0.0.0:8000 application:app
