"""
装饰器：
        @property
        @属性.setter
简化私有属性访问方式
"""
class Account():
    def __init__(self):
        self.__money=0
    @property#在获取money的时候被调用
    def money(self):
        return self.__money
    @money.setter#在设置money的时候被调用
    def money(self,money):
        if isinstance(money,int):
            self.__money=money
        else:
            raise TypeError('注释')
m=Account()
print(m.money)
m.money=55
print(m.money)