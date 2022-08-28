#形参用于定义的 时候；实参用于调用的时候
def print_min(x,y):
    '''判断两个数字，输出最小值'''
    if x>y:
        print('最小值：',y)
    else:
        print('最小值：',x)
    return x+y

def print_hello():
    '''return的用法'''
    print('&&&&&&&&&&&&')
    return 8

print(print_hello())
print(print_min(15,7))
help(print_min.__doc__)#调用函数的补充说明