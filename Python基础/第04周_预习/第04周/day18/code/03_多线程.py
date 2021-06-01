# 多线程
import time
import random
import threading
# 子线程
def thread(*args):
    time.sleep(random.random())
    print(args)


if __name__ == '__main__':
    '''
    # 创建多个线程
    t1 = threading.Thread(target=thread, args=('喜羊羊',))
    t1.start()
    t1.join()  # 暂停等待t1执行完成后,再执行后面代码

    t2 = threading.Thread(target=thread, args=('美羊羊',))
    t2.start()
    t2.join()

    t3 = threading.Thread(target=thread, args=('懒羊羊',))
    t3.start()
    t3.join()
    '''

    # 统计时间
    start = time.time()

    # 使用for循环
    t_list = []
    for i in range(1, 11):
        t = threading.Thread(target=thread, args=(f'thread-{i}',))
        t.start()
        # t.join()   # 同步
        t_list.append(t)

        # 其他的方法: 了解
        # print(t.name)    # 线程名
        # print(t.daemon)   # 是否为守护线程, False
        # print(t.ident)  # 线程号
        print(t.is_alive())  # 是否正在运行
        print(threading.enumerate())  # 列举所有线程
        print(threading.active_count())  # 正在运行的线程数量


    # # 要在创建好10个线程后,再去等待10个线程都要执行完,才统计时间
    for t in t_list:
        t.join()

    end = time.time()
    print(end - start)