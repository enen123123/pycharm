#.py后缀为模块,四种东西
a=0#1.变量
def b():#2，函数
    print('success')
    pass
class Teacher:#3.面向对象
    def __init__(self,name):
        self.name=name
    def score(self):
        print(self.name)
Teacher('we').score()#4.可执行代码
print(a)
b()



