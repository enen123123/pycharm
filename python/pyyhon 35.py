#实现最大值、最小值判断
def max(a,b):
    if a > b:
        return a
    else:
        return b
def min(a,b):
    if a < b:
        return a
    else:
        return b
a=4
b=3
print('max=',max(a,b))
print('min=',min(a,b))