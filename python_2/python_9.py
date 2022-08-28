#单工聊天
from socket import *
s=socket(AF_INET,SOCK_DGRAM)
s.bind(('192.168.195.54',8088)) #bind:设置绑定ip，端口
s.sendto('连接成功!!!'.encode('gb2312'),('192.168.195.54',8585))#送往python_10的端口
redate=s.recvfrom(1024)
print(redate[0].decode('gb2312'))

#只实现数据的接受
#先运行python_10，在运行python_9