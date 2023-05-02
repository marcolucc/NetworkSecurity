from scapy.all import *
import random

def send_syn(dst_ip, dst_port):
    src_port = random.randint(1025, 65535)
    syn_packet = IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="S")
    syn_ack_packet = sr1(syn_packet)
    if syn_ack_packet and syn_ack_packet.haslayer(TCP):
        if syn_ack_packet.getlayer(TCP).flags == 0x12:
            send_ack(dst_ip, dst_port, syn_ack_packet.getlayer(TCP).seq + 1, syn_ack_packet.getlayer(TCP).ack)
        else:
            print("Port {} closed".format(dst_port))

def send_ack(dst_ip, dst_port, seq_num, ack_num):
    ack_packet = IP(dst=dst_ip) / TCP(sport=random.randint(1025, 65535), dport=dst_port, flags="A", seq=seq_num, ack=ack_num)
    send(ack_packet)

if __name__ == '__main__':
    target_ip = "192.168.1.1"
    target_port = 80
    send_syn(target_ip, target_port)
