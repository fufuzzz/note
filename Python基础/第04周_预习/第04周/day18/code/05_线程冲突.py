import threading

# 线程冲突: 多个线程使用同一个资源时,造成的冲突问题
# 解决方式: 用线程锁

n = 0
def f1():
    global n
    for i in range(1000000):
        n += 1

    print(n)

# 线程冲突
def create_thread1():
    for i in range(3):
        threading.Thread(target=f1).start()


lock = threading.Lock()
def f2():
    # 添加锁: 自动加锁, 自动解锁
    with lock:
    # with rlock:   # 递归锁
        global n
        for i in range(1000000):
            n += 1

        print(n)

    # 手动加锁
    # lock.acquire()  # 锁住
    # global n
    # for i in range(1000000):
    #     n += 1
    #
    # print(n)
    # lock.release()  # 解锁
# 线程冲突
def create_thread2():
    for i in range(3):
        threading.Thread(target=f2).start()


if __name__ == '__main__':
    create_thread2()


# 死锁:
#   thread1  thread2
#       A       B
#       B       A

# 递归锁/重用锁:
#   解决死锁
