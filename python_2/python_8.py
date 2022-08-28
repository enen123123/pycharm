from socket import *
s=socket(AF_INET,SOCK_DGRAM)#ipv4,UDP
address=('192.168.35.54',8080)
date=input('输入发送的内容：')
s.sendto(date.encode('gb2312'),address)#sendto：发送数据
#encode()：改变数据流，'gb2312'：网络调试助手的字符集,'UTF-8':python的字符集['192.168.35.54':ip地址][8088:端口网络:用来输入端口号]，sendto():数据发送
redate=s.recvfrom(1024)#recvfrom：接受数据
#1024:所能接受的最大数据
print(redate[0].decode('gb2312'),redate[1])
#[0]：选择第一个元素，[1]：ip和端口，decode('gb2312')：解码
s.close()