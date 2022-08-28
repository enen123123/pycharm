#隐藏嵌套函数，姓、名判断
def a0(isb,name1,name2):
    def aa0(a,b):
        print("{0}{1}".format(a,b))
    if isb:
        aa0(name2,name1)
    else:
        aa0(name1,name2)
a0(True,'小五','格斗-')
a0(False,'野原','-小新')