#测试拼接符号join or +

import time

time1=time.time()#初始时刻
a=' '
for i in range(1000000):
    a+='@'
time2=time.time()#结束时刻
print("第一次计算时间为："+str(time2-time1))


time3=time.time()
li=[ ]
for i in range(1000000):
    li.append('@')

a=''.join(li)
time4=time.time()
print("第二次计算时间为："+str(time4-time3))

#推荐使用join
