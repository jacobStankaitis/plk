FROM python:3
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt

ADD . /code/

WORKDIR /code/

CMD python3 manage.py runserver 0.0.0.0:8000