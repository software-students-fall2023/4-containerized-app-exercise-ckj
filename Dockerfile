FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY machine_learning_client.py .

COPY webapp.py .

CMD ["python", "webapp.py"]
