#第2种导入自定义模块方式
import python_37#模块名不能有空格
x=8
y=3
print('max=',max(x,y))
print('min=',min(x,y))
print('------')
#第2种导入自定义模块方式
from python_37 import max,min#*可代替max,min，相当于全部函数,不能贴加全局变量
print('max=',max(x,y))
import package.python_2