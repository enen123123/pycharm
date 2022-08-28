#作为TCP的服务端，先开服务端，和python_18链接，
#网络地址一定一定一定要是正确的写法，最好是复制，cmd->ipconfig,
from socket import *
tcp_sock=socket(AF_INET,SOCK_STREAM)#SOCK_STERAM:TCP协议
tcp_addr=('192.168.223.54',8099)#设置服务器地址，端口必须在0-65535内
tcp_sock.bind(tcp_addr)
tcp_sock.listen(5)#限制最大连接数
new_sock,client_addr=tcp_sock.accept()#accept:用来等待连接，一旦有客户端连接，就会收到两个数据
#新的套接字，连接方的地址

data=new_sock.recv(1024)#TCP使用recv
print(data)
new_sock.send('Thank you'.encode())#TCP使用send

new_sock.close()#关闭发送地址

tcp_sock.close()#关闭接受数据
