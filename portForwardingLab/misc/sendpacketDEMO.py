#import scapy and create a packet
from scapy.all import *
packet = IP(dst="0.0.0.0")/ICMP()
#send the packet
send(packet)

#send the packet 10 times
send(packet, count=10)
