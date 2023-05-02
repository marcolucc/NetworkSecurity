FROM alpine:3.15

# Install the packages for the services
RUN apk --no-cache add openssh nginx vsftpd

# Configure SSH
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    echo "root:password" | chpasswd

# Configure Nginx
RUN echo "hello world" > /var/www/localhost/htdocs/index.html && \
    sed -i 's/80/8080/g' /etc/nginx/http.d/default.conf

# Configure vsftpd
RUN adduser -D ftpuser && \
    echo "ftpuser:password" | chpasswd && \
    echo "anonymous_enable=YES" >> /etc/vsftpd/vsftpd.conf && \
    echo "local_enable=YES" >> /etc/vsftpd/vsftpd.conf && \
    echo "write_enable=YES" >> /etc/vsftpd/vsftpd.conf && \
    echo "chroot_local_user=YES" >> /etc/vsftpd/vsftpd.conf && \
    echo "user_sub_token=$USER" >> /etc/vsftpd/vsftpd.conf && \
    echo "local_root=/home/$USER/ftp" >> /etc/vsftpd/vsftpd.conf

RUN ssh-keygen -A

# Expose the ports for the services
EXPOSE 22 8080 21

# Start the services
CMD /usr/sbin/sshd && nginx && vsftpd
