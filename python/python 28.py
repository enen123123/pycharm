#测试组合
class A:#使用继承实现代码复用,is
    def say1(self):
        print('a1,a1,a1')
class B(A):
    pass
a1=B()
a1.say1()
print()

class AA:#使用组合实现代码复用,has
    def say2(self):
        print('a2,a2,a2')
class BB:
    def __init__(self,n):
        self.n=n
a2=AA()
b=BB(a2)
b.n.say2()