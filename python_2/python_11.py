#半双工聊天室
from socket import *
s=socket(AF_INET,SOCK_DGRAM)
s.bind(('192.168.35.54',8089)) #bind:设置绑定ip，端口
s.sendto('连接成功!!!'.encode(),('192.168.35.54',8590))
redate=s.recvfrom(1024)
print(redate[0].decode())#描述接受的数据

#实现数据的接受和传送
#先运行python_12，在运行python_11