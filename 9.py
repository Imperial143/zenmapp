9a
nc -l -p 8080 < image.jpg
or 
printf "HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\n\r\n" | cat - lion.jpeg | nc -l -p 8080
http://localhost:8080

9b

nc -l -p 5000
http://localhost:5000

in terminal after few seconds 

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Server: nooblinux

Hello from Netcat!

4c nmap -sn 127.0.0.100-200
nmap -sn 127.0.0.0/24
