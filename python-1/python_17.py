"""
    xx      一般情况下使用
    _xx     模块中，无法使用from import*调用
    __xx    私有属性方法，只能在类内使用，（改名）_类__私有属性名 或 _类__私有方法名
    __xx__  用于方法。__init__ __del__ __new__ __str__ 系统自动调用，避免重名
    xx_     区别变量名，方法名

    dir()   访问属性
"""
#import python_18
#print(python_18.pi)
from python_18 import*
print(pi)