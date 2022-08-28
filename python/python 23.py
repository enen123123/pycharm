class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#私有属性
    def say_age(self):
        print('self.__age:',self.__age)
    def say_in(self):
        print('ma name:',self.name)
class Teacher(Student):
    def __init__(self,name,age,score):
        Student.__init__(self,name,age)#必须显示的调用父类初始化方法，不然不会被调用
        self.score=score
    def say_in(self):
        print('改写成功')
a=Teacher('野原',5,77)
a.say_age()
a.say_in()
