def chu(a,b):
    print('商=',a/b)
a=input('a=')
b=input('b=')
if a.isdigit() and b.isdigit():#验证a,b为纯数字
    a=int(a)#将字符串a改为数字,str->int
    b=int(b)#b!=0,分母不为零
    if b!=0:
        chu(a,b)
    else:
        print('b=0,分母不能为0')
else:
    print('数字类型错误,请重新输入：')




