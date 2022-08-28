"""
    Python 3.10(python-1)->python->Doc->python3100.chm#查看documentation功能书
    浅复制
        copy.copy()
    深复制
        copy.deepcopy()
        复合对象：对象里面加对象:[1,1,2,[4,3,2]]
"""
import copy
list1=[1,1,2]
list2=copy.copy(list1)#复制改变地址id
list3=copy.deepcopy(list1)#深可以复制复合对象中对象的地址id，浅复制只能复制值value
print('list1=',list1)
print('list2=',list2)
print('list3=',list3)
print(list2 is list3)
print('id(list1)=',id(list1))
print('id(list2)=',id(list2))
print('id(list3)=',id(list3))

list4=[2,4]
list5=[5,4]
list6=[list4,list5]#深复制可以复制复合对象中对象的地址id，浅复制只能复制值value
list7=copy.copy(list6)
list8=copy.deepcopy(list6)
print('copy.copy(list6)=',copy.copy(list6))
print('copy.deepcopy(list6)=',copy.deepcopy(list6))
print('id(copy.copy(list6))=',id(copy.copy(list6)))
print('id(copy.deepcopy(list6))=',id(copy.deepcopy(list6)))
print('id(list6[0])',id(list6[0]))
print(list7[0] is list6[0])#浅
print(list8[0] is list6[0])#深
#print('id(list7[0])',id(list7[0]))
#print('id(list8[0])',id(list8[0]))