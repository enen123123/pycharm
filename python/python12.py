
a=10#全局变量
def print_test(x,y):
    b=2#局部变量
    global a#改变全局变量
    a=5
    print(a+b)
    return 0
print_test(6,7)
print(a)