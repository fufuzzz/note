
# greenlet + sleep : 了解

import time
from greenlet import greenlet


def fn1():
    print('协程1')
    time.sleep(3)
    g2.switch()  # 切换到协程2

    print('hello')
def fn2():
    print('协程2')
    time.sleep(3)
    g1.switch()

if __name__ == '__main__':
    g1 = greenlet(fn1)
    g2 = greenlet(fn2)
    g1.switch()  # 切换到协程1