#对象、类
class Student:#首字母大写
    def __init__(self,name,score):#self必须第一位
        self.name=name
        self.score=score
    def say_score(self):
        print("{0}的分数为：{1}".format(self.name,self.score))
a1=Student('蜡笔',5)
a1.say_score()

a1.see=88
a1.dee=99
print(a1.dee,a1.see)
Student.say_score(a1)
print(dir(a1))#获得所有函数
print(a1.__dict__)#获得定义函数
print(isinstance(a1,Student))#判断前者属于后者
class Man:
    pass#空语句
