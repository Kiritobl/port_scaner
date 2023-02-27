from scapy.all import *
import time
import re



def ARP_scan(IP):

    if not (re.match(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', IP) or re.match(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])./[0-3][0-9]$',IP)):
         return('非法输入,请输入主机IP地址或网段')

    all=''
    t1=time.time()
    p=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=IP)
    ans,unans=srp(p,timeout=5)
    all+=("一共扫描到"+str(len(ans))+"台主机：\n")
    result=[]
    for s,r in ans:
        result.append([r[ARP].psrc,r[ARP].hwsrc])
    result.sort()
    all+='ARP扫描存活的ip地址：\n'
    for ip,mac in result:
        all+=(str(ip)+'\n')
    t2 = time.time()
    all+=('所用时间为：'+str((int(t2 - t1)))+'s\n')
    print (all)
    return all
    
if __name__ == '__main__':
    
    ip = '192.168.3.25/24'
    threadnum = 20
    ARP_scan(ip)