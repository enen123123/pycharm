"""
验证is和==
==浅层次的
is深层次的id,type,value

pycharm：浅层次
ipython：深层次
ipython的界限为-5~256
-5~256为默认的地址，所以地址相同，超出范围则重新赋予地址
"""
"""
Python 3.10(python-1)->python->Doc->python3100.chm#查看documentation功能书
"""
a=2
b=2
print(a==b)
print(a is b)
print(id(a))
print(id(b))
