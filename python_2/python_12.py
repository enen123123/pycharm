from socket import *

UDPsock=socket(AF_INET,SOCK_DGRAM)
UDPsock.bind(('192.168.35.54',8590))
while True:#（多次运行）
    recv_date=UDPsock.recvfrom(1024)
    print(recv_date[0].decode())#查看python_11接受的数据
    date=input('请输入:')#描述数据
    UDPsock.sendto(date.encode(),recv_date[1])#送往python_11的端口

UDPsock.close()