#列表输出字典

a1={'name':'小以','age':'45','weight':'66kg'}
a2={'name':'小二','age':'84','weight':'74kg'}
a3={'name':'小三','age':'26','weight':'35kg'}

x=[a1,a2,a3]



for i in range(len(x)):
    #for j in range(2):
        print(x[i].get ('name'),x[i].get ('age'),x[i].get ('weight'))


b={'id':'地址','type':'类型','value':'值'}
print(b)
