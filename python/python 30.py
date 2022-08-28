#测试工厂模式
class SchoolFactory:
    def create(self,ty):
        if ty=='语文':
            return Teacher()
        elif ty=='数学':
            return Student()
        elif ty=='英语':
            return Cleaner()
        else:
            return "无法识别"
class Teacher:
    pass
class Student:
    pass
class Cleaner:
    pass
factory=SchoolFactory()
a1=factory.create('语文')
a2=factory.create('数学')
a3=factory.create('英语')
a4=factory.create('历史')
print(a1)
print(a2)