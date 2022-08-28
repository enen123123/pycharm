#私有属性
class Person:
    __home='野原'
    def __init__(self,name,age):#私有属性
        self.name=name
        self.__age=age
    def __say(self):#私有方法
        print('work work hard!')
        print("self.__age=",self.__age)
        print(Person.__home)
c=Person('幅度',18)
print(c.name)
print(c._Person__age)
print(dir(c))
c._Person__say()
print(Person._Person__home)