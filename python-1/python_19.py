class School():
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def getname(self):
        return self.name
    def getage(self):
        return self.__age
    def setgae(self,age):
        if isinstance(age,int):#判断age类型
            self.__age=age
        else:
            raise TypeError('类型错误（可删除，删除后只弹出前面的错误类型）')#raise用来抛出一个错误类型
    age=property(getage,setgae)#合并两个函数，使__xx类型的值便于调用

s=School('大使馆',44)
print(s.age)
#s.setgae(33)
s.age=33.3
print(s.age)