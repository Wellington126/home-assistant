FROM python:3.12-slim
RUN pip install paho-mqtt
COPY subscriber.py /subscriber.py
CMD ["python", "-u", "/subscriber.py"]
