class Student:#类方法
    company='ads'
    @classmethod
    def print(cls):#必须cls
        print(cls.company)
Student.print()
#类方法和静态方法不能调用实例变量和方法
class Student:#静态方法
    company='hjg'
    @staticmethod
    def print1(a,b):
        print('a+b=',a+b)
Student.print1(1,2)