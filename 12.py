12 a
nano traceroute.py
from scapy.all import *
# Perform traceroute to multiple targets
result, unanswered = traceroute(
    ["www.example.com", "www.google.com"],
    maxttl=20
)
# Display result
result.show()
sudo python3 traceroute.py

12b
nc -l -p 8080 < image.jpg
or 
printf "HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\n\r\n" | cat - lion.jpeg | nc -l -p 8080
http://localhost:8080

12 c
Badstore
