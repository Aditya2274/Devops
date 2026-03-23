FROM python:3.11-slim

WORKDIR /myapp

COPY ./sql_demo.py .
COPY ./servers.txt .

RUN python -m pip install --no-cache-dir pymysql cryptography

CMD ["python", "sql_demo.py"]