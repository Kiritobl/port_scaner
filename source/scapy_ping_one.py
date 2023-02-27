from scapy.all import *
from random import randint

def scapy_ping_one(host):
 id_ip = randint(1, 65535)
 id_ping = randint(1, 65535)
 seq_ping = randint(1, 65535)
 packet = IP(dst=host, ttl=128, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b'Kirito says hello to you  (:'
 ping = sr1(packet, timeout=0.5, verbose=False)
 if ping:
    print(str(host)+'done')
    return 1
 else:
   return 0

def scapy_ping_one_alive(host):
 id_ip = randint(1, 65535)
 id_ping = randint(1, 65535)
 seq_ping = randint(1, 65535)
 packet = IP(dst=host, ttl=128, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b'Kirito says hello to you  (:'
 ping = sr1(packet, timeout=5, verbose=False)
 if ping:
    print(str(host)+'alive')
    return 1
 else:
    print(str(host)+' not alive')
    return 0
    
if __name__ == '__main__':
 scapy_ping_one('192.168.3.24')