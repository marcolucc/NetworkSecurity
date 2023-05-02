from scapy.all import *

# Set the source and destination IP addresses
src_ip = "localhost"
dst_ip = "0.0.0.0" 

#Set the destination port numbers
dst_port = 1234

# Create the IP packet
ip_packet = IP(src=src_ip, dst=dst_ip)

# Create the TCP packet
tcp_packet = TCP( dport=dst_port)

# Combine the packets and send them
packet = ip_packet / tcp_packet
send(packet)
