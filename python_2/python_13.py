#TFTP简单文件下载
import struct#新模式
from socket import *


cmb_buf=struct.pack('!H7sb5sb',1,b'lei.png',0,b'octet',0)#struct.pack：整合数据流字节包
#设置文件格式，!:指定数据的格式，H：将1替换为两个字节，7s（sssssss）：代表几个字符,b:一个字节
udp_sock=socket(AF_INET,SOCK_DGRAM)
udp_sock.sendto(cmb_buf,('192.168.195.54',8088))
f=open('lei.png','ab')
#a:以追加模式打开，若没有文件，则创建一个新的文件
#b:以二进制的形式打开

