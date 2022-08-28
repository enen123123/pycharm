from socket import*
client_d=socket(AF_INET,SOCK_STREAM)
client_d.connect(('192.168.223.54',8298))
client_d.send('测试多进程1'.encode('gb2312'))
date=client_d.recv(1024)
print(date)
client_d.close