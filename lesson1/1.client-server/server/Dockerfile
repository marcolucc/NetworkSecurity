# Base image
FROM alpine:latest

# Install necessary packages
RUN apk add --no-cache tcpdump

# Create directory to store captured data
RUN mkdir /data

# Set tcpdump command to continuously capture packets and write to a file
CMD ["tcpdump", "-i", "eth0", "-w", "/data/captured_packets.pcap"]