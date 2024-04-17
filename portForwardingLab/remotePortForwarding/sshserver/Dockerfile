FROM ubuntu:latest
# Install SSH server
RUN apt-get update && \
 apt-get install -y openssh-server curl
# Create an SSH user
RUN useradd -rm -d /home/sshuser -s /bin/bash -g root -G sudo -u 1000 sshuser
# Set the SSH user's password 
RUN echo 'sshuser:password' | chpasswd
# Allow SSH access
RUN mkdir /var/run/sshd
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
#gateway ports to allow remote port forwarding
RUN echo 'GatewayPorts yes' >> /etc/ssh/sshd_config
# Allow SSH user to run sudo without password
RUN echo 'sshuser ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
#permit open 
RUN echo 'PermitOpen any' >> /etc/ssh/sshd_config
#allow tcp forwarding
RUN echo 'AllowTcpForwarding yes' >> /etc/ssh/sshd_config
#allow agent forwarding
RUN echo 'AllowAgentForwarding yes' >> /etc/ssh/sshd_config

# Expose the SSH port
EXPOSE 22
# Start SSH server on container startup
CMD ["/usr/sbin/sshd", "-D"]