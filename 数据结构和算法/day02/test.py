class Node():
    def __init__(self, item):
        self.elem = item
        self.next = None


class RoundLinklist:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def append(self, item):
        cur = self.head
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = node

        while cur.next != self.head:
            cur = cur.next

        node.next = cur.next
        cur.next = node

    def travel(self):
        pass





if __name__ == '__main__':
    r = RoundLinklist()
