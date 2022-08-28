from multiprocessing import Pool
import time
def work(num):
    print(num)
    time.sleep(1)
if __name__=="__main__":
    pool=Pool(2)#不写的话默认为cpu数,该电脑为四核八线程cpu
    for i in range(20):
        pool.apply_async(work,(i,))
        #apply_async:无阻塞类型
        #apply:阻塞方式，同一时间只有一个，类似于单线程
        #terminate:无论何时，立即强制关闭
    pool.close()#关闭进程，不再接受新的任务
    pool.join()#join必须在close后面