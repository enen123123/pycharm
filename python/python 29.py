#组合的使用例子，手机
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
a=Phone(Cpu(),Key())
a.cpu.suan()
a.key.show()
