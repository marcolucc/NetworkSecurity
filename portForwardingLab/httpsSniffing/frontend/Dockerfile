FROM nginx:alpine 
COPY nginx.conf /etc/nginx/conf.d/default.conf
#copy the cert and key to the container
COPY nginx-selfsigned.crt /etc/nginx/cert.pem
COPY nginx-selfsigned.key /etc/nginx/key.pem
RUN apk add --no-cache openssh curl openssh-client

