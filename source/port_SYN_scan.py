import queue
import threading
from scapy.all import *
from testping import check_online

'''
功能介绍：
    通过TCPSYN进行端口扫描，需要用户输入ip,port,线程数(默认10)
'''
res=''
def Portscan_Threadfun(ip):                         
    while True:
        if q.empty():                              
            break
        else:
            port = q.get()                    
            Portscan_SYN(ip, port)


def Portscan_SYN(ip, port):
    try:
        temp = sr(IP(dst=ip) /TCP(dport=(int(port)), flags='S'),timeout=2, verbose=False)
        if temp[0].res:
            result = temp[0].res                   
            if (result[0][1].payload.flags) == 'SA':
                print('端口开放')
                openport_list.append(port)
                return 1
            else:
                closeport_list.append(port)
        else:
            closeport_list.append(port)
            return 0
    except:
        closeport_list.append(port)
        return 0

def Portscan_print(ip):                            
    openport_list.sort()
    for i in openport_list:
        print(ip + "\t" + str(i) + " Open\t\t")
    closeport_list.sort()
    for i in closeport_list:
        print(ip + "\t" + str(i) + " Close")


def Portscan_threadnum(ip, num=10):                
    thread_joinlist = []
    for i in range(0, num):                        
        new_thread = threading.Thread(target=Portscan_Threadfun, args=(ip,))
        new_thread.start()
        thread_joinlist.append(new_thread)
    for i in thread_joinlist:
        i.join()                                 

def Portscan_synport(ip,userport=0,threadnum=20):
    if not re.match(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', ip):
         return('非法输入,请输入主机IP地址或网段')
    if check_online(ip=ip)==0:
         return('目标主机未开机')
    global q
    global openport_list
    global closeport_list
    global res
    res=''
    openport_list = []
    closeport_list = []
    q = queue.Queue()
    if userport:
        if ',' in userport:
            ports = userport.split(',')
        elif '-' in userport:
            ports = userport.split('-')
            tmpports = []
            [tmpports.append(i) for i in range(int(ports[0]), int(ports[1]) + 1)]
            ports = tmpports
        else:
            ports = [userport]
    else:
        print('Default Ports')
        ports = [21, 22, 23, 53, 80, 111, 139, 161, 389, 443, 445, 512, 513, 514,1080,135,139,
                 873, 1025, 1433, 1521, 3128, 3306, 3311, 3312, 3389, 5432, 5900,
                 5984, 6082, 6379, 7001, 7002, 8000, 8080, 8081, 8090, 9000, 9090,
                 8888, 9200, 9300, 10000, 11211, 27017, 27018, 50000, 50030, 50070]

    [q.put(i) for i in ports]                           #将端口加入队列
    Portscan_threadnum(ip,threadnum)
    Portscan_print(ip)
    for i in openport_list:
        res+=(str(i)+'端口开放\n')
    if len(res)==0:
        return('未检测到开放端口')
    return res


if __name__ == '__main__':
    ip = '38.6.229.21'
    Portscan_synport(ip,threadnum=10)
