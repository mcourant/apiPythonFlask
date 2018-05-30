FROM python:3

ADD app.py /
ADD common /common
ADD resources /resources
ADD config /config

RUN pip install pymysql
RUN pip install flask_restful

CMD [ "python", "./app.py" ]