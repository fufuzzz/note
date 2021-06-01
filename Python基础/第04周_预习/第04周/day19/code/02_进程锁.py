import multiprocessing
import time

def fn1(i, lock):
    with lock:
        print('子进程开始i =', i)
        time.sleep(4)
        print('子进程结束i =', i)

def fn2(i, sem):
    with sem:
        print('子进程开始i =', i)
        time.sleep(4)
        print('子进程结束i =', i)


if __name__ == '__main__':
    # 进程锁
    # lock = multiprocessing.Lock()
    #
    # for i in range(1, 6):
    #     multiprocessing.Process(target=fn1, args=(i, lock)).start()



    信号量: 一般是核数的两倍左右
    sem = multiprocessing.Semaphore(8)
    for i in range(1, 6):
        multiprocessing.Process(target=fn2, args=(i, sem)).start()
