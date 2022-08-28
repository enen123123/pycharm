"""
    进制
    二进制：bin()
    八进制 oct()
    十六斤进制 hex()
    十进制 int('a',b)#b=几进制，a=几进制的数字
十进制转换，÷其他进制，取余数，倒叙，前项0不计
M进制转换，365=5*10^0+6*10*1+3*10^2
"""
num=100
a=bin(num)
print(a)
print(type(a))

a1=oct(num)
print(a1)
print(type(a1))

a2=hex(num)
print(a2)
print(type(a2))

a3=int('0x64',16)
print('0x64的十进制=',a3)
a3=int('0o144',8)
print('0o144的十进制=',a3)
a3=int('0b1100100',2)
print('0b1100100的十进制=',a3)