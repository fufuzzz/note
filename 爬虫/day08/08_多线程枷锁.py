from threading import Thread, Lock

l = Lock()
a = 0

def run1():
    global a
    for i in range(10000000):
        l.acquire()  #加锁
        a += 1
        l.release()  # 解锁

def run2():
    global a
    for i in range(100000):
        l.acquire()
        a += 1
        l.release()

if __name__ == '__main__':
    t1 = Thread(target=run1)
    t2 = Thread(target=run2)
    t1.start()
    t2.start()
    t1.join()
    t1.join()
    print(a)