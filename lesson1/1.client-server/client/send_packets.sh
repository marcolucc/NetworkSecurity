#!/bin/bash

# Set the packet payload to send
PAYLOAD="Hello, world!"

# Continuously send packets to the server
while true; do
  curl --data "$PAYLOAD" $SERVER_HOST:$SERVER_PORT
done