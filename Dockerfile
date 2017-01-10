FROM python:2.7.12

RUN pip install kafka-python
RUN pip install flask

COPY . /opt/

ENTRYPOINT [ "python", "./opt/main.py" ]
