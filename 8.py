8a
import socket

target_ip = socket.gethostbyname("www.example.com")
print("Target IP:", target_ip)


from scapy.all import *
import socket

target_ip = socket.gethostbyname("www.example.com")

ports = [22, 80, 443]

print(f"Scanning target: {target_ip}")

for port in ports:
    packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)

    if response:
        if response.haslayer(TCP):
            if response[TCP].flags == "SA":
                print(f"Port {port} is OPEN")
                
                send(IP(dst=target_ip)/TCP(dport=port, flags="R"), verbose=0)
                
            elif response[TCP].flags == "RA":
                print(f"Port {port} is CLOSED")
    else:
        print(f"Port {port} is FILTERED or NO RESPONSE")

8b 
nmap --script vuln 127.0.1.1

nmap --script vuln 127.0.1.1 -oN txtgh.txt

8c Badstore
