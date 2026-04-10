10a
nano icmp_monitor.py

from scapy.all import *

# Callback function (runs every time a packet is captured)
def packet_callback(packet):
    
    # Check if packet has IP layer
    if packet.haslayer(IP):
        
        # Check if protocol is ICMP (protocol number = 1)
        if packet[IP].proto == 1:
            print(f"ICMP packet detected from {packet[IP].src} to {packet[IP].dst}")

# Start sniffing
sniff(prn=packet_callback, filter="icmp", store=0)


sudo python3 icmp_monitor.py

in another terminal run
ping 8.8.8.8

5b
nmap 127.0.1.1
nmap -sV 127.0.1.1

