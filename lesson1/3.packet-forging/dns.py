from scapy.all import *

# Send an ARP request to the destination IP address to get its MAC address
result, unanswered = arping("0.0.0.0")

# Extract the MAC address from the response
mac_address = result[0][1].hwsrc

# Create a DNS request packet for www.google.com
dns_request = Ether()/IP(dst="0.0.0.0")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="www.google.com"))

# Set the destination MAC address in the Ethernet header
dns_request[Ether].dst = mac_address

# Send the packet and receive the response
dns_response = sr1(dns_request, verbose=0)

# Print the response
dns_response.show()
