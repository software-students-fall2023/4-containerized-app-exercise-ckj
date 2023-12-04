FROM python:3.9.6

WORKDIR /webapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "webapp.py"]