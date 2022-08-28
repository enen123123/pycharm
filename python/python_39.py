#使用其他文件夹中的模块，其一
print(max(3,6))
import sys#下方添加相应模块的具体位置
sys.path.append('D:\文件夹\桌面\python-1')
a=sys.path
for i in a:
    print(i)
import python_2
print(python_2.add(3,2))#需要将模块以及函数都写出来