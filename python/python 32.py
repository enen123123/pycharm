#单例模式、工厂模式混用
class School:
    a = None
    aa = True
    def create(self,ty):
        if ty=='语文':
            return Teacher()
        elif ty=='数学':
            return Student()
        elif ty=='英语':
            return Cleaner()
        else:
            return "无法识别"
    def __new__(cls, *args, **kwargs):
        if cls.a==None:
            cls.a=object.__new__(cls)
        return cls.a
    def __init__(self,name):
        if School.aa==True:
            School.aa =False
            print('question')
            self.name=name
class Teacher:
    pass
class Student:
    pass
class Cleaner:
    pass
factory=School('g')
a1=factory.create('语文')
a2=factory.create('数学')
a3=factory.create('历史')
print(a1)
print(a2)

factory2=School('')
print(factory2)
print(factory)