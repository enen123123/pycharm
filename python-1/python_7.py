#try/except/else/finally
try:
    file=open('123txt','w',encoding='utf-8')#w:即使文件存在，创建文件
    file.write('hello world!')
    file.write('1,2,3')
    print('写入完成')
except:
    print('error')
else:
    print('no error')
finally:
    file.close()
    print('成功关闭')