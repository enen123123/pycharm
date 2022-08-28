#lambda简单函数,匿名函数
x=lambda a,b,c:a+b+c
print(x)
print(x(1,2,3))

y=[lambda a:a*2,lambda a:a*3,lambda a:a*4]
print(y[0](3),y[1](3),y[2](3))