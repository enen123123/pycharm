#作为TCP的客户端,
#网络地址一定一定一定要是正确的写法，最好是复制，cmd->ipconfig
from  socket import*
client_sock=socket(AF_INET,SOCK_STREAM)
client_sock.connect(('192.168.223.54',8099))#connect:链接服务器
client_sock.send('you are welcome'.encode())
date=client_sock.recv(1024)
print(date)
client_sock.close()



