
import copy
class Phone:
    def __init__(self,cpu,key):
        self.cpu=cpu
        self.key=key
class Cpu:
    def suan(self):
        print('算数')
        print('cpu对象=',self)
class Key:
    def show(self):
        print('显示画面')
        print('key对象',self)
a1=Cpu()
a2=a1
print(a1)
print(a2)
#浅复制
s1=Key()
q1=Phone(a1,s1)
q2=copy.copy(q1)
print(q1,q1.cpu,q1.key)
print(q2,q2.cpu,q2.key)
#深复制
q3=copy.deepcopy(q1)
print(q1,q1.cpu,q1.key)
print(q3,q3.cpu,q3.key)
