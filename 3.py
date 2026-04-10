sudo python3
from scapy.all import *
result, unanswered = traceroute(["www.example.com", "www.google.com"], maxttl=20)
result.show()

3b
nc example.com 80
GET / HTTP/1.1
Host: example.com

HEAD / HTTP/1.1
Host: example.com

3c 
nmap -sn 127.0.0.1

nmap -sn 127.0.0.1/24
