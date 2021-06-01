import time
import threading
import random

# 信号量: 控制线程的最大并发数量
sem = threading.Semaphore(4)


def fn(*args):
    with sem:
        print(args)
        time.sleep(random.randint(1, 3))
        print(args, '=>finish')


for i in range(1, 21):
    threading.Thread(target=fn, args=(i,)).start()
