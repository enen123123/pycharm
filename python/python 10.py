#函数的调用
def a ( ):
    print('sdfgh')


print(id(a()))
print()
print(type(a()))
print()
for i in range(5):
    a()
