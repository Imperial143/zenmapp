11a
nano scap.py 
import scapy.all as scapy

request = scapy.ARP()
request.pdst = "192.168.5.0/24"

broadcast = scapy.Ether()
broadcast.dst = "ff:ff:ff:ff:ff:ff"

request_broadcast = broadcast / request

clients = scapy.srp(request_broadcast, timeout=1, verbose=False)[0]

for element in clients:
    print(element[1].psrc + "  " + element[1].hwsrc)

 sudo python3 scap.py 


11b
nc -l -p 8080 < image.jpg
or 
printf "HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\n\r\n" | cat - lion.jpeg | nc -l -p 8080
http://localhost:8080

11 c Badstore
