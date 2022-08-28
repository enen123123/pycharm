class Error(BaseException):#自定义异常
    def __init__(self):
        super().__init__()
        self.error='自定义异常'

class Teacher():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def xingbie(self,gender):
        if gender=='男' or gender=='女':
            return self.gender
        else:
            raise Error()


    def show(self):
        print('name=%s,xingbie=%s'%(self.name,self.gender))
try:
    t=Teacher('撒旦','9')
    t.show()
except BaseException as e:
    print(e.error)
try:
    t.xingbie('🚹')
except BaseException as e:
    print(type(e))
    print(e.args)
    print(e.error)

