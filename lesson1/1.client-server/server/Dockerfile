FROM alpine:latest

RUN apk update && apk add netcat-openbsd

EXPOSE 1234

#CMD nc -l -p 1234 -k | while read line; do echo "Packet received"; done
#make the container run forever
CMD tail -f /dev/null