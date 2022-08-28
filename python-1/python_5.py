#异常处理，使用try:和except:
def chu(a,b):
    print('商=',a/b)
a=input('a=')
b=input('b=')
try:#异常处理，节省代码长度，与python_4对比
    a=int(a)
    b=int(b)
    chu(a,b)
except:
    print('数字类型错误/分母不为0')