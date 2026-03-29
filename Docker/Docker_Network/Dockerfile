FROM python

WORKDIR /myapp

COPY ./sql_demo.py .

RUN pip install pymysql
RUN pip install cryptography

CMD ["python","sql_demo.py"]