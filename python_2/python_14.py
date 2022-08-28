#Tftpd64软件,TFTP下载文件
import struct
from socket import*
file_name='lei.png'#文件名
server_ip='192.168.195.54'#服务器地址
send_date=struct.pack('!H%dsb5sb'%len(file_name),1,file_name.encode(),0,'octet'.encode(),0)
s=socket(AF_INET,SOCK_DGRAM)
s.sendto(send_date,(server_ip,69))#服务器端口69是用来监听的
f=open(file_name,'ab')
while True:
    recv_date=s.recvfrom(1024)
    #print(recv_date)#查看接收的数据
    cao_zuo_ma,ack_num=struct.unpack('!HH',recv_date[0][:4])
    #recv_date[0][:4]：recv_date中的第一个元素的前四个元素
    rand_port=recv_date[1][1]#获取随机端口号
    if int(cao_zuo_ma)==5:#操作码是5就是错误包
        print('no file...')
        break
    print('操作码：%d, ACK:%d, 服务器随机端口:%d, 数据长度:%d'%(cao_zuo_ma,ack_num,rand_port,len(recv_date[0])))
    f.write(recv_date[0][4:])#[4:]从第四个之后
    if len(recv_date[0])<516:
        break
    ack_num=struct.pack('!HH',4,ack_num)
    s.sendto(ack_num,(server_ip,rand_port))

