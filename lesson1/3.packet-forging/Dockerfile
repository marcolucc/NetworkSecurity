FROM python:3.9-slim-buster

RUN pip install scapy

WORKDIR /app

COPY tcp-packet.py .

CMD ["python", "tcp-packet.py"]
