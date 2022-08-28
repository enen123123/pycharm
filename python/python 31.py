#测试单例模式
class As:
    a=None
    aa=True
    def __new__(cls, *args, **kwargs):
        if cls.a==None:
            cls.a=object.__new__(cls)
        return cls.a
    def __init__(self,name):
        if As.aa==True:
            As.aa =False
            print('question')
            self.name=name
b=As('bb')
c=As('cc')
print(c)
print(b)
