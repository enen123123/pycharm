#import socket#使用比较麻烦
#from socket import *#方便
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#AF_INET:IPV4  SOCK_STREAM:UDP协议和TCP协议，两者不能串起来用
#UDP:ip和端口就可以发数据（不建立链接），流模式，速度快，丢数据，黑客攻击
#TCP:需要建立链接（打招呼，确立身份），才可以收发数据，数据包模式，速度慢，通信稳定，不丢数据
