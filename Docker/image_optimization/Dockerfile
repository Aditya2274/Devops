FROM python:3.11-slim

WORKDIR /myapp

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY app.py .

CMD ["python","app.py"]