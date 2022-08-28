
b1={'name':'小以','age':18,'work':3000}
b2={'name':'小儿','age':32,'work':5000}
b3={'name':'小三','age':11,'work':3000000}
a=[b1,b2,b3]
for i in a:
    if i.get('age')<20:
        print(i)
    else:
        continue