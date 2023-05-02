from scapy.all import *

ip = "192.168.1.1"  # Replace with your desired IP address

packet = IP(dst=ip) / ICMP()
reply = sr1(packet, timeout=1)

if reply is not None:
    print(f"Response received from {reply.src}")
else:
    print("No response received")
