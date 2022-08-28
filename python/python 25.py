#运算符改写
class Person:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        if isinstance(other,Person):
            return (self.name,other.name)
        else:
            return '不是同类对象'
a1=Person('野原')
a2=Person(77)
x=a1+a2
print(x)