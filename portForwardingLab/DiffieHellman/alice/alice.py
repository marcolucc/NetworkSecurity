import socket
import math

# Constants
p = 23  # prime number
g = 5   # generator
private_key_alice = 6
message = 3

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('172.28.0.3', 1234)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

# Compute public key
public_key_alice = (g ** private_key_alice) % p

# Send public key to Bob
sock.sendall(str(public_key_alice).encode())

# Receive Bob's public key
public_key_bob = int(sock.recv(1024).decode())

# Compute shared secret
shared_secret = (public_key_bob ** private_key_alice) % p

# Encrypt and send message to Bob
encrypted_message = (message * shared_secret) % p
sock.sendall(str(encrypted_message).encode())

print("Message sent to Bob:", message)

# Close the connection
sock.close()
