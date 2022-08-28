"""
模块导入：
        1.import 模块名1，模块名2
    使用：
        1.模块名.变量
        2.模块名.函数名(参数)
        3.模块名.类
    导入数据：
        from 模块 inport 变量，函数，类
        导入后可直接输用
"""
import random#导入模块
result0=random.randint(1,9)
print(result0)
from random import randint#导入模块相关数据
result1=randint(1,6)
print(result1)