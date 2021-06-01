# 定义节点

class Node():
    def __init__(self, item):
        self.elem = item
        self.next = None


# 定义ADT
class SingleLinkList():

    # 初始化这个类对象,要表示是一个空链
    def __init__(self):
        self.head = None

    # 链表是否为空
    def is_empty(self):
        return self.head == None

    # 链表长度
    def length(self):
        # 创建计数器
        count = 0

        # 创建指针
        cur = self.head

        # while 循环
        while cur != None:
            count += 1
            cur = cur.next

        return count

    # 遍历整个链表self,
    def travel(self, ):
        # 判断链表是否为空
        if self.is_empty():
            print('')
        else:
            # 创建指针, 指向第一个节点
            cur = self.head

            # while 循环, 打印 每一个节点的元素
            while cur != None:
                print(cur.elem, end=' ')
                cur = cur.next
            print()

    # 链表头部添加元素
    def add(self, item):
        # 创建节点
        node = Node(item)

        # 把新节点的next指向到第一个节点
        node.next = self.head

        # 把头部指向到新节点
        self.head = node

    # 链表尾部添加元素
    def append(self, item):
        # 创建新节点
        node = Node(item)

        # 判断链表是否为空
        if self.is_empty():
            self.head = node
        else:
            # 创建指针, 指向到第一个节点
            cur = self.head

            # while循环,找到链表中最后一个节点
            while cur.next != None:
                # 指针一直往后移动
                cur = cur.next

            # 跳出循环, cur所在位置就是最后一个节点
            # 那就把 cur 的next指向新节点
            cur.next = node

    # 指定位置添加元素
    # 如果pos <= 0, 直接使用在头部插入
    # 如果pos > self.length(), 直接使用在尾部插入
    def insert(self, pos, item):

        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            count = 1
            # 创建指针
            cur = self.head
            # while 循环
            while count < pos:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            cur.next = node


    # 删除节点
    def remove(self, item):
        cur = self.head
        pre = Node(None)
        while cur != None:
            if cur.elem == item:
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next




    # 查找节点是否存在
    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    s = SingleLinkList()
    s.append(10)
    # s.travel()
    s.append(20)
    s.append(30)
    s.add(100)
    s.insert(2, 50)
    s.remove(20)
    s.travel()
    print(s.search(20))
    print(s.length())