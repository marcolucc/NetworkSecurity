FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y net-tools iputils-ping tcpdump

#make the container run forever
CMD tail -f /dev/null

