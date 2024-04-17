#simple socket that accepts a connection and sends a message back
import socket

def main():
    #create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket to the address and port
    s.bind(('0.0.0.0', 12345))
    #listen for a connection
    s.listen(5)
    #accept the connection
    c, addr = s.accept()
    print('Got connection from', addr)
    #send a message back
    c.send(b'Thank you for connecting')
    #close the connection
    c.close()

if __name__ == '__main__':
    main()