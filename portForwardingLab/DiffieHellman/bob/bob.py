import socket
import math

# Constants
p = 23  # prime number
g = 5   # generator
private_key_bob = 15

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('bob', 1234)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive Alice's public key
        public_key_alice = int(connection.recv(1024).decode())

        # Compute public key
        public_key_bob = (g ** private_key_bob) % p

        # Send public key to Alice
        connection.sendall(str(public_key_bob).encode())

        # Compute shared secret
        shared_secret = (public_key_alice ** private_key_bob) % p

        # Receive and decrypt message from Alice
        encrypted_message = int(connection.recv(1024).decode())
        message = (encrypted_message * shared_secret) % p
        print("Message received from Alice:", message)

    finally:
        # Clean up the connection
        connection.close()
