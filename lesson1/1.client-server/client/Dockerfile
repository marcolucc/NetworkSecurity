# Base image
FROM alpine:latest

# Install necessary packages
RUN apk add --no-cache curl

# Set environment variables
ENV SERVER_HOST=server
ENV SERVER_PORT=5000

# Copy script to send packets continuously
COPY send_packets.sh /send_packets.sh

# Set the script as the entrypoint
ENTRYPOINT ["/send_packets.sh"]