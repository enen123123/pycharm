from socket import *
#数据接收
UDPsock=socket(AF_INET,SOCK_DGRAM)
UDPsock.bind(('192.168.195.54',8585))
while True:
    recv_date=UDPsock.recvfrom(1024)
    UDPsock.sendto(recv_date[0],recv_date[1])

UDPsock.close()#关闭程序
