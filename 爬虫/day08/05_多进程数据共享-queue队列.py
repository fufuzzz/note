from multiprocessing import Process,Manager,Queue

# lis = []
# dic = []

def run1(q):
    # q.put是往队列中放入数据
    q.put('run1')


def run2(q):
    # q.get()是从队列中获取数据
    print(q.get())
    q.put('run2')


if __name__ == '__main__':

    q = Queue()

    # 创建进程
    p1 = Process(target=run1, args=(q, ))
    p2 = Process(target=run2, args=(q, ))

    # 执行进程
    p1.start()
    p2.start()

    # 阻塞,必须等待在这两个进程执行完之后, 再打印lis
    p1.join()
    p2.join()
    a = q.get()
    print(a)
