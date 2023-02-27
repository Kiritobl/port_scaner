import subprocess
import re
import threading
from queue import Queue
import ipaddress
import time

all=[]


def IP_list (net_ips):
  ip_list = Queue()

  net=ipaddress.ip_network(net_ips)
  for IP in net:
    ip_addr=str(IP)
    ip_list.put(ip_addr)
  return ip_list



#定义 ping 函数
def ping_IP (IP_QUEUE):
  while not IP_QUEUE.empty():
    ip = IP_QUEUE.get().strip('\n')
    #print (ip)
    res = subprocess.call('ping -w 1000 -n 1 %s' % ip , stdout=subprocess.PIPE,shell=True)
    #print (res)
    if res == 0:
      h =subprocess.getoutput('ping' + ' ' + ip)
    #print (h)

      if 'TTL=' in h:
        all.append(ip)
        return 1
      else: 
        return 0
def ping_cmd (net_ips):
  global all
  all=[]
  t1=time.time()
  if not (re.match(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', net_ips) or re.match(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])./[0-3][0-9]$',net_ips)):
         return('非法输入,请输入主机IP地址或网段')
  IP_LIST = IP_list(net_ips)
  threads = []
  THREAD_NUM = 20
  IP_L = IP_LIST
  for i in range (THREAD_NUM):
    t = threading.Thread(target = ping_IP,args = (IP_L,))
    threads.append(t)
  for i in range (THREAD_NUM):
    threads[i].start()
  for i in range (THREAD_NUM):
    threads[i].join()
  print(all)
  t2=time.time()
  res=''
  res+=('一共扫描到'+str(len(all))+'台主机\n')
  res+='ICMP扫描存活主机ip地址：\n'
  for i in all:
    res+=i
    res+='\n'
  res+=('所用时间为：'+str((int(t2 - t1)))+'s\n')
  return res
if __name__ == '__main__':
  net_ips='192.168.3.0/24'
  ping_cmd(net_ips)