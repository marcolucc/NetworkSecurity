FROM alpine:latest
RUN apk add --no-cache bash netcat-openbsd

#CMD while true; do echo "Packet sent" | nc -w 1 server 1234; sleep 1; done
#make the container run forever
CMD tail -f /dev/null