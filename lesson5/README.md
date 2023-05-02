# ARP spoofing
Overview: In this lab, you will learn how to use the Address Resolution Protocol (ARP) to map IP addresses to MAC addresses on a local network. You will use the ARP utility to display and manipulate the ARP cache on a Linux system, and you will also use Wireshark to capture and analyze ARP traffic on the network.

## Prerequisites:

-  Build the Docker containers provided

To build the container, save the Dockerfile to a directory on your local machine and run the following command from that directory:

`docker build -t arp-lab .` 

This will create a new image named `arp-lab` based on the Dockerfile. You can then start a container based on this image using the following command:

`docker run -it arp-lab` 

This will start a container with a Bash shell, where you can run the ARP lab commands and experiment with ARP on the local network.

Note that the container may need to be run in privileged mode or with additional network configuration options to capture network traffic with `tcpdump`.


## Objectives:

-   Understand the purpose and operation of ARP
-   Use the ARP utility to display and manipulate the ARP cache
-   Use Wireshark to capture and analyze ARP traffic

## Steps:

1.  Start by opening a terminal on the Linux system that you will be using for this lab.
    
2.  Use the `ifconfig` command to identify the network interface that is connected to the local network. Note the IP address and MAC address of the interface.
    
3.  Use the `arp` command to display the current contents of the ARP cache:
    
    
    `arp -a` 
    
    This will display a list of IP addresses and corresponding MAC addresses that have been resolved using ARP.
    
4.  Use the `ping` command to send a few ICMP echo request packets to another host on the local network:
    
    
    `ping <IP address of the other host>` 
    
    This will cause the Linux system to send ARP requests to resolve the MAC address of the destination host.
    
5.  Use the `arp` command again to display the updated contents of the ARP cache:
    

    `arp -a` 
    
    You should see the IP address and MAC address of the destination host that was pinged.
    
6.  Use Wireshark to capture the ARP traffic on the local network. Start a new capture and filter the packets by ARP protocol:
    
    `arp` 
    
7.  Repeat step 4 by pinging the same destination host again. Observe the ARP packets in Wireshark and note the source and destination MAC addresses.
    
8.  Stop the Wireshark capture and analyze the ARP packets. Note the ARP operation (request or reply), source and destination MAC addresses and IP addresses, and the ARP payload (the MAC address being requested or provided).
    
9.  Use the `arp` command to delete an entry from the ARP cache:
    
    `arp -d <IP address>` 
    
    This will delete the specified IP address and corresponding MAC address from the ARP cache.
    
10.  Use Wireshark to capture the ARP traffic again and observe the ARP packets generated when an ARP entry is deleted.

## ARP spoofing
See arp0,  arp1, arp2 folders