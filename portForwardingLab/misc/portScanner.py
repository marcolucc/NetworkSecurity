#port scanner using sockets
import socket

for port in range(1, 1025):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            s.connect(('0.0.0.0', port))
            print(f'Port {port} is open')
    except:
        pass

print('Port scanning complete')