#UDP广播
from socket import*
dest=('192.168.195.54',8080)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.sendto('你好 world!!!'.encode('gb2312'),dest)
while True:
    recv_data=s.recvfrom(1024)
    print(recv_data[0].decode('gb2312'))



