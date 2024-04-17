from scapy.all import *

def show_3way_handshake():
    #send SYN
    ip = IP(src="127.0.0.1", dst="127.0.0.1")
    syn = TCP(dport=80, flags="S", seq=100)
    synack = sr1(ip/syn)
    #send SYN-ACK
    ack = TCP(dport=80, flags="A", seq=synack.ack, ack=synack.seq + 1)
    send(ip/ack)
    #send ACK
    data = "GET / HTTP/1.1\r\nHost:0.0.0.0\r\n\r\n"
    ack = TCP(dport=80, flags="PA", seq=synack.ack, ack=synack.seq + 1)
    send(ip/ack/data)
    #receive data
    data = sr1(ip/ack/data)
    print(data)

show_3way_handshake()