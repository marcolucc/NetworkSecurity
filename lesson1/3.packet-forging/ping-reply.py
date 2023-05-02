from scapy.all import *

def reply_echo_request(packet):
    if packet.haslayer(ICMP) and packet[ICMP].type == 8: # ICMP Echo Request
        print(f"Received ICMP Echo Request from {packet[IP].src}")
        reply = IP(src=packet[IP].dst, dst=packet[IP].src) / ICMP(type=0, id=packet[ICMP].id, seq=packet[ICMP].seq) / packet[Raw]
        send(reply)
        print(f"Sent ICMP Echo Reply to {packet[IP].src}")

sniff(filter="icmp", prn=reply_echo_request)
