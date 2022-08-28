import multiprocessing
import time
class Myprocess(multiprocessing.Process):
    def paint(self):
        n=0
        print(333)
        while n<5:
            print(n)
            #time.sleep(1)
            n+=1
if __name__ =="__main__":
    p=Myprocess()
    p.start()
    p.join()
