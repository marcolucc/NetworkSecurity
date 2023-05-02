FROM python:3.9

RUN apt-get update && apt-get install -y nano

WORKDIR /app

COPY . main.py

#make the container run forever
CMD tail -f /dev/null
