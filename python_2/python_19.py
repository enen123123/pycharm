#多进程
#python_19|20|21|22  对应多进程|多线程|测试0端口|测试1端口
#每个端口对应进程、线程的端口不同、ip相同
from socket import*
from multiprocessing import*#使用多进程模块,例如Process
from time import sleep

def deal_client(new_socket,dest_addr):
    while True:
        recv_date=new_socket.recv(1024)
        if len(recv_date)>0:#一般发送一个长度为0的数据包，来表示数据传输完成
            print('recv%s:%s'%(str(dest_addr),recv_date.decode('gb2312')))
        else:
            print('%s客户端已经关闭'%str(dest_addr))
            break
    new_socket.close()

def main():
    ser_socket=socket(AF_INET,SOCK_STREAM)
    ser_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    #setsockopt:为了能够重复使用同一个地址
    local_addr=('192.168.223.54',8298)
    ser_socket.bind(local_addr)
    ser_socket.listen(5)

    try:#异常处理
        while True:
            print('~~~主程序，等待新客户端的到来~~~')
            new_socket,dest_addr=ser_socket.accept()
            print('~~~主程序，接下来创建一个新的进程负责数据处理~~~')
            client= Process(target=deal_client,args=(new_socket,dest_addr))
            #创建进程，target：执行函数deal_client，args：传递数据
            client.start()
            new_socket.close()#若是改为多线程需要去掉本行，且Process(进程)需要改为threading(线程)
    finally:
        ser_socket.close()
if __name__=='__main__':
    main()

