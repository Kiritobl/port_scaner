

1.运行环境：
Windows10操作系统
python 3.10
scapy 2.4.5
tkinker 8.6

2.文件列表
/source 源代码
主程序：scan.py
主机扫描：ARP_one.py   ping_cmd.py  testping.py
端口扫描：port_connect_scan.py  port_FIN_scan.py  port_SYN_scan.py
/bin  /build python打包配置文件
/bin  /dist 可运行文件

2.主要算法。
主机发现中，通过ARP和ICMP两种包实现，在对单个IP进行搜索时，用scapy模块构造对应的数据包并通过sr()函数监听网卡获取返回包并分析。在对网段进行检索时，ARP向广播地址发包并监听返回包，ICMP通过多线程方式向网段中主机发包并监听返回包。
端口扫描中，通过scapy模块构造不同的包来实现不同方式的端口扫描，并通过多线程方式检测目标主机端口是否开放。