import multiprocessing
import time
"""
#两种方法，任选
    def test(self):#run是个函数方法
        n=0
        while n<5:
            print(n)
            time.sleep(1)
            n+=1
if __name__ =="__main__":
    p = multiprocessing.Process(target=test)
    p.start()
    p.join()
"""
class Myprocess(multiprocessing.Process):
    def run(self):#run是个函数方法，更改系统中的run函数
        n=0
        while n<5:
            print(n)
            time.sleep(1)
            n+=1
if __name__ =="__main__":

    p = Myprocess()
    p.start()
    p.join()
