#sys.path用来存储列表，如：random,time,pygame,tulter
import sys#系统模块sys
sys.path
print(type(sys.path))
for i in sys.path:#查看当前文件夹下的函数
    print(i)
print('分割行~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#import random#在当前文件夹下建立一个random的模块，若是这边建立random，会覆盖系统本身的random
#a=random.test()#测试手动和默认的random优先级，因系统之间产生冲突，已经删除，格式类似于python_11
import python_11
python_11.test()
"""
    路径的表达形式：
                1：D:/文件夹/桌面/python-1/python_9.py
                2：D:\\文件夹\\桌面\\python-1\\python_9.py
"""
sys.path.append('D:\\文件夹\\桌面\\python-1\\python_9.py')#手动加入一个自己建立的模块，例如python_9
for i in sys.path:#遍历是否增加了所需要的函数
    print(i)
import python_9
python_9.Test().test()
