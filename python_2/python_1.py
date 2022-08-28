#import multiprocessing
from multiprocessing import Process#调用部分multiprocessing的功能
def paint(name,age):
    print('qwerg %s %s'%(name,age))
def paint1():
    print('87645')
#那个进程先跑，跑得快，取决于系统的调度
if __name__=='__main__':#子进程里__name__不等于'__main__  为了让其只在主进程调用
    #__name__：python的内置变量，当前模块的名字
    p=Process(target=paint,name='进程一',args=('test',12))#位置参数元组
        #Process：用来创造进程  name:用来改进程名  target：选择调用的函数  args：传递函数的参数，位置参数元组,必须是元组，只有一个元素时必须加逗号
    p.start()#让进程跑起来
    print(p.name)#打印进程名字，默认是Process-1
    p.join()#join:防止主进程结束，子进程还未结束，让主进程等一会
    p1=Process(target=paint1)
    p1.start()
    p1.join()

"""

p=Process()
p.pid()#系统分配的程序id，让系统识别
p.start()#启动程序
p.run()#进程启动
p.terminate()#中止进程，大量垃圾
p.is_alive()#判断当前是否运行
p.join([timeout])#让主进程等待子进程，[]:一般是可选的，timeout：等待时间
"""