from threading import Thread

a = 0

def run1():
    global a
    for i in range(10000000):
        a += 1

def run2():
    global a
    for i in range(100000):
        a += 1


if __name__ == '__main__':
    t1 = Thread(target=run1)
    t2 = Thread(target=run2)
    t1.start()
    t2.start()
    t1.join()
    t1.join()
    print(a)