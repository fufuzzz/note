from linklist import SingleLinkList
# 定义节点
class Node():
    def __init__(self, item):
        self.pre = None
        self.elem = item
        self.next = None



class DoubleLinkList(SingleLinkList):

    def __init__(self):
        # SingleLinkList.__init__(self, )
        super(DoubleLinkList, self).__init__()

    def is_empty(self):
        return self.head == None

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
            # node.pre指向cur
            node.pre = cur

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            # 把新节点的next指向到第一个节点
            node.next = self.head

            self.head.pre = node

            # 把头部指向到新节点
            self.head = node

    def insert(self, pos, item):

        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            count = 0
            # 创建指针
            cur = self.head
            # while 循环
            while count < pos:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.pre = cur.pre
            cur.pre.next = node
            cur.pre = node

    def remove(self, item):
        cur = self.head
        while cur != None:
            if cur.elem == item:
                if cur == self.head:
                    self.head = cur.next
                    if cur.next:
                        cur.next.pre = None
                else:
                    if cur.next:
                        cur.next.pre = cur.pre
                    cur.pre.next = cur.next
                return
            else:

                cur = cur.next


if __name__ == '__main__':
    d = DoubleLinkList()
    d.append(20)
    d.append(30)
    d.append(40)
    d.add(100)
    d.remove(40)
    d.travel()