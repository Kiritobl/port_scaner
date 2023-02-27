import time
from scapy_ping_one import scapy_ping_one
from scapy.all import *



def ICMP_scan(aIP):



    all=''
    t1=time.time()
    
    ans,unans= srp(Ether(dst="ff:ff:ff:ff:ff:ff")/IP(dst=aIP)/ICMP(),timeout=5)
    all+=("一共扫描到"+str(len(ans))+"台主机：\n")
    result=[]
    for r,s in ans:
        result.append(r[IP].dst)
    result.sort()
    all+='ICMP扫描存活的ip地址：\n'
    for ip in result:
        all+=(str(ip)+'\n')
    t2 = time.time()
    all+=('所用时间为：'+str((int(t2 - t1)))+'s\n')
    print (all)
    return all
    
if __name__ == '__main__':
    
    ip = '111.6.167.0/24'
    threadnum = 20
    ICMP_scan(ip)