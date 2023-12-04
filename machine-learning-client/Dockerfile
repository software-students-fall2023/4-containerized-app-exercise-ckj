FROM python:3.9.6

WORKDIR /ml_client

COPY requirements.txt ./

RUN pip install -r requirements.txt

ADD ml_client/ . /

CMD ["python", "ml_client.py"]