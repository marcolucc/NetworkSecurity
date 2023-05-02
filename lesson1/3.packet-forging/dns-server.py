from scapy.all import *

def dns_server(pkt):
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        # This is a DNS query
        print("Received DNS query for", pkt.qd.qname.decode())
        dns_resp = IP(dst=pkt[IP].src, src=pkt[IP].dst)/UDP(dport=pkt[UDP].sport, sport=53)/\
            DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, an=DNSRR(rrname=pkt.qd.qname, rdata='1.2.3.4'))
        send(dns_resp, verbose=0)
        print("Sent DNS response")

# Start sniffing DNS traffic on port 53
sniff(filter="udp port 53", prn=dns_server)
