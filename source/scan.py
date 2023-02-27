from tkinter import *
from ARP_one import ARP_scan
from ping_cmd import ping_cmd
from port_connect_scan import Portscan_portlist_co
from port_SYN_scan import Portscan_synport
from port_FIN_scan import Portscan_portlist
def button_event():
    print("按钮按下\n")
    return
def button_close():
    var1.set('')
    var2.set('')
    var3.set('')
    var4.set('')
def  ARP():
    text.config(state='normal')
    ip=var1.get()
    res=ARP_scan(ip)
    text.delete(1.0,END)
    text.insert(INSERT,res)
    text.config(state='disabled')
def  ICMP():
    text.config(state='normal')
    text.delete(1.0,END)
    text.insert(INSERT,'waiting.......')
    ip=var2.get()
    res=ping_cmd(ip)
    text.delete(1.0,END)
    text.insert(INSERT,res)
    text.config(state='disabled')
def port_connect():
    text.config(state='normal')
    userport=var4.get()
    if userport=='':
        userport=0
    ip=var3.get()
    text.delete(1.0,END)
    res=Portscan_portlist_co(ip=ip,userport=userport)
    text.insert(INSERT,res)
    text.config(state='disabled')
def port_syn():
    text.config(state='normal')
    userport=var4.get()
    if userport=='':
        userport=0
    ip=var3.get()
    text.delete(1.0,END)
    res=Portscan_synport(ip=ip,userport=userport)
    text.insert(INSERT,res)
    text.config(state='disabled')
def port_fin():
    text.config(state='normal')
    userport=var4.get()
    if userport=='':
        userport=0
    ip=var3.get()
    text.delete(1.0,END)
    res=Portscan_portlist(ip=ip,userport=userport)
    text.insert(INSERT,res)
    text.config(state='disabled')
#创建窗口
root = Tk()
#设置窗口
#设置标题
#设置大小
#设置可变属性
root.geometry('1050x700+200+200')
root.title('主机发现&端口扫描工具')

string1=''

ARP_BU = Button(root, text ="ARP扫描", command = ARP,background='light blue')
ARP_BU.place(x=250,y=70)
ICMP_BU =Button(root, text ="ICMP扫描", command = ICMP,background='light blue')
ICMP_BU.place(x=250,y=180)
port_connect=Button(root, text ="TCP_connect端口扫描", command = port_connect,background='light blue')
port_connect.place(x=40,y=400)
port_syn=Button(root, text ="TCP_syn端口扫描", command = port_syn,background='light blue')
port_syn.place(x=40,y=450)
port_fin=Button(root, text ="TCP_fin端口扫描", command = port_fin,background='light blue')
port_fin.place(x=40,y=500)

l1=Label(text='ARP扫描,请输入IP或网段',bd=1,relief=SUNKEN,font=('楷体',15))
l1.place(x=5,y=40)
l2=Label(text='ICMP扫描,请输入IP或网段',bd=1,relief=SUNKEN,font=('楷体',15))
l2.place(x=5,y=150)
l3=Label(text='端口扫描,请输入IP与扫描端口\n端口号可使用“,”或“-”连接\n 若不输入端口将检测常用端口',bd=1,relief=SUNKEN,font=('楷体',15))
l3.place(x=5,y=250)
C=Button(root, text ="清空所有输入框", command = button_close,background='light blue')
C.place(x=230,y=340)

var1 = StringVar() 
var2 = StringVar() 
var3 = StringVar() 
var4 = StringVar() 
var3.set('请在此输入主机IP地址')
var4.set('请在此输入端口号')

e1=Entry(root,bd=3,textvariable=var1)
e1.place(x=40,y=70)
e2=Entry(root,bd=3,textvariable=var2)
e2.place(x=40,y=180)

port_port=Entry(root,bd=3,textvariable=var4,name='asd')
port_host=Entry(root,bd=3,textvariable=var3)
port_host.place(x=40,y=330)
port_port.place(x=40,y=360)

yscrollbar = Scrollbar(root)
text = Text(root,height=50,width=80,state='disabled',font='20')
yscrollbar.pack(side=RIGHT,fill=Y)
text.place(x=350,y=0)
yscrollbar.config(command=text.yview)
text.config(yscrollcommand=yscrollbar.set)


root.mainloop()
