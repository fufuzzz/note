
import gevent

def fn1():
    print('协程1')
    gevent.sleep(2)
    print('协程1-2')


def fn2():
    print('协程2')
    gevent.sleep(4)
    print('协程2-2')


if __name__ == '__main__':
    g1 = gevent.spawn(fn1)
    g2 = gevent.spawn(fn2)
    gevent.joinall([g1, g2])