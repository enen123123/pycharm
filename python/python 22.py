#测试技巧
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#私有属性
    def say_age(self):
        print('i don not know')
class Teacher(Student):
    def __init__(self,name,age,score):
        Student.__init__(self,name,age)#必须显示的调用父类初始化方法，不然不会被调用
        self.score=score
print(Teacher.mro())
a=Teacher('野原',5,100)
a.say_age()
print(a.name)
print(dir(a))
print(a._Student__age)
