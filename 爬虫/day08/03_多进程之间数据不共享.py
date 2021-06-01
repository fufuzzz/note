from multiprocessing import Process

lis = []


def run1():
    lis.append('run1')


def run2():
    lis.append('run2')


if __name__ == '__main__':

    # 创建进程
    p1 = Process(target=run1)
    p2 = Process(target=run2)

    # 执行进程
    p1.start()
    p2.start()

    # 阻塞,必须等待在这两个进程执行完之后, 再打印lis
    p1.join()
    p2.join()

    print(lis)