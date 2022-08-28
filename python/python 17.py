class Teacher:
    name='美亚'   #类属性
    count=0      #类属性
    def __init__(self,a,b):
        self.a=a    #实例属性
        self.b=b
        Teacher.count=Teacher.count+1
    def say_student(self):  #实例方法
        print('Teacher.name',Teacher.name)
        print("self.b",self.b)
        print("self.a", self.a)
s1=Teacher('阿斯顿',77)    #s1是实例对象，自动调用__init__()方法
s1.say_student()
print('创建了{0}个Teacher对象'.format(Teacher.count))



