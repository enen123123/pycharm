#测试特殊属性
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,n):
        self.n=n
    def c(self):
        print('c=')
c=C(3)
print('0=',dir(c))
print('1=',c.__class__)
print('2=',c.__dict__)
print('3=',C.__bases__)
print('4=',C.mro())
print('5=',A.__subclasses__())