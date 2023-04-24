# NetworkSecurity

# Lab Course Description

This lab course lasts for 12 hours and covers various topics related to network traffic analysis and anomaly detection.

https://www.corsi.univr.it/?ent=cs&id=417&menu=Studiare&tab=Insegnamenti&codiceCs=S71&codins=4S008904&crediti=6.0&aa=2023/2024&lang=it

## Network Traffic Analysis

The following topics will be covered:

-   Common packet filtering systems (firewalls) and an introduction to Netcat, Wireshark, and tcpdump.
-   Writing a port scanner in Python and an introduction to the nmap tool.
-   Physical addresses and the ARP protocol, ARP tables, and ARP spoofing attacks. The concept of ARP poisoning and the use of the Ettercap tool. Detection modes of ARP spoofing attacks and risk mitigation.
-   An overview of HTTP header stripping modes. SSLStrip and Bettercap tools. The limitations of the network layer as a defense mechanism for application-level attacks.

## Anomaly Detection in Network Traffic

The following topics will be covered:

-   Log analysis for attack detection. An overview of the configuration modes of IPS and IDS based on logs.
-   Common network-level configuration errors and their associated risks at higher levels. Major vulnerabilities in web applications resulting from network layer issues, such as security misconfigurations (A5), sensitive data exposure (A6), and the use of known vulnerable components (A9), as well as the theft of authentication credentials, session tokens, and sensitive information. Examples of ARP poisoning.
-   The Linux Netfilter firewall, its functionality and operation modes, tables, chains, rules, targets, and default policies. An overview of QoS and its use for connections that require specific latency guarantees. An overview of filtering rule optimization modes to improve filtering efficiency.
-   Netfilter extensions for connection state matching (new, established, related, and invalid), address types (unspec, local prohibit, unicast, broadcast), comments, limits and burst concepts, MAC address filtering, and the use of the firewall to mitigate ARP spoofing attacks.

## Verification of Network Traffic Filtering and IDS Configurations

The following topics will be covered:

-   Designing an IDS system. Activating IDS for a web infrastructure example. Implementing an IPS system for brute-force attacks on FTP credentials and port scanning. Writing an IPS prototype using the iptables firewall and the Linux shell. An overview of the OSSEC IPS.
-   Case study: SYN flood attacks (half-open attacks) and mitigation strategies, including limiting the resources consumed by the attack using network tools.
-   Considerations regarding the effectiveness of security through progressive network closures.
-   Comparison of the Netfilter firewall with CISCO's ASA (briefly) and PF (BSD systems).
-   A guided exercise on using the pfSense (community edition) enterprise firewall, including connection wrapping functions, port forwarding, and filtering rule definition for embedded systems using the OpenWRT firewall.

# Requirements 

1.  Python: Python can be downloaded and installed from the official website [https://www.python.org/downloads/](https://www.python.org/downloads/). Follow the instructions on the website to install Python on your system.
    
2.  Scapy: Scapy can be installed using pip, the Python package installer. Open a terminal and run the following command:
    

`pip install scapy` 

3.  Netcat: Netcat can be installed using your system's package manager. For example, on Ubuntu, you can install Netcat by running the following command:

`sudo apt-get install netcat` 

4.  Wireshark: Wireshark can be downloaded and installed from the official website [https://www.wireshark.org/#download](https://www.wireshark.org/#download). Follow the instructions on the website to install Wireshark on your system.
    
5.  Docker: Docker can be downloaded and installed from the official website [https://www.docker.com/get-started](https://www.docker.com/get-started). Follow the instructions on the website to install Docker on your system.
    

Note that the above instructions assume that you are using a Linux-based operating system. If you are using a different operating system, the installation instructions may be slightly different.