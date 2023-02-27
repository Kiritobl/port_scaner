import queue
import socket
import threading
import re
from testping import check_online

def Portscan_Threadfun(ip):                      
    while True:
        if q.empty():                              
            break
        else:
            port = q.get()                          
            Portscan_TCPconnect(ip, port)


def Portscan_TCPconnect(ip, p):                    
    try:
        port = int(p)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if port == 3306 or port == 22 or port == 23 or port == 1521:
            s.settimeout(4)
        else:
            s.settimeout(1)
        s.connect((ip, port))
        openport_list.append(port)
    except Exception as e:
        closeport_list.append(port)
    finally:
        s.close()


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


def Portscan_portlist_co(ip, threadnum=20, userport=0):   
    global q
    global openport_list
    global closeport_list
    res=''
    if not re.match(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', ip):
         return('非法输入,请输入主机IP地址或网段')
    if check_online(ip=ip)==0:
         return('目标主机未开机')
    q = queue.Queue()
    openport_list = []
    closeport_list = []
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
        ports = [5708,21, 22, 23, 53, 80, 111, 139, 161, 389, 443, 445, 512, 513, 514,1080,135,
                 873, 1025, 1433, 1521, 3128, 3306, 3311, 3312, 3389, 5432, 5900,
                 5984, 6082, 6379, 7001, 7002, 8000, 8080, 8081, 8090, 9000, 9090,
                 8888, 9200, 9300, 10000, 11211, 27017, 27018, 50000, 50030, 50070]
    [q.put(i) for i in ports]                       
    Portscan_threadnum(ip, threadnum)
    Portscan_print(ip)                              
    for i in openport_list:
        res+=(str(i)+'端口开放\n')
    if len(res)==0:
        return('未检测到开放端口')
    return res

if __name__ == '__main__':
    
    ip = '192.168.3.24'
    threadnum = 20
    Portscan_portlist_co(ip, threadnum,)
