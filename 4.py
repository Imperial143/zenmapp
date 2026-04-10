ifconfig
nano scanner.py
inside 
import scapy.all as scapy

request = scapy.ARP()
request.pdst = "10.0.2.15/24"   

broadcast = scapy.Ether()
broadcast.dst = "ff:ff:ff:ff:ff:ff"

request_broadcast = broadcast / request

clients = scapy.srp(request_broadcast, timeout=1)[0]

print("IP Address\t\tMAC Address")
print("-----------------------------------------")

for element in clients:
    print(element[1].psrc + "\t\t" + element[1].hwsrc)

sudo python3 scanner.py

4b
nc -l -p 5000
http://localhost:5000

in terminal after few seconds 

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Server: nooblinux

Hello from Netcat!

4c 
nmap -sn 127.0.0.100-200
nmap -sn 127.0.0.0/24
