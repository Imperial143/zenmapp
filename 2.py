2a badstore
2b
sudo python3
from scapy.all import *
pac=sniff(count=10)
pac.summary()

2c
1st termianl
nc -vlp 1234
2nd terminal
nc localhost 1234
