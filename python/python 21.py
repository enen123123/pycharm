#测试
class Person:

    def __init__(self,name,age):
        self.name=name
        self.__age=age

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            print('error')

'''
    def get_age(self):
        return self.__age
    def set_age(self,age):

        if 0<=age<=100:
            self.__age=age
        else:
            print('error')

a1=Person('刚好',78)
print(a1.get_age())
a1.set_age(77)
print(a1.get_age())'''
a1=Person('刚好',788)
print(a1.age)
a1.age=88
print(a1.age)