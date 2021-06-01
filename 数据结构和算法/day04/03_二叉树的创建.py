# 创建树的节点
class Node:
    def __init__(self, elem):
        self.left = None
        self.elem = elem
        self.right = None



class Tree:
    def __init__(self):
        self.root = None


    def add(self, elem):
        # 创建节点
        node = Node(elem)
        lis = [self.root]
        # 判断是否是空节点
        if self.root == None:
            self.root = node
            return self.root
        while lis:
            cur_node = lis.pop(0)
            if cur_node.left == None:
                cur_node.left = node
                return
            else:
                lis.append(cur_node.left)
            if cur_node.right == None:
                cur_node.right = node
                return
            else:
                lis.append(cur_node.right)

    # 广度优先
    def travel(self):
        if self.root == None:
            print('')
        else:
            lis = [self.root]
            while lis:
                cur_one = lis.pop(0)
                print(cur_one.elem, end=' ')
                if cur_one.left != None:
                    lis.append(cur_one.left)
                if cur_one.right != None:
                    lis.append(cur_one.right)

    # 先序遍历
    def preorder(self, root):
        if root == None:
            return
        print(root.elem)
        self.preorder(root.left)
        self.preorder(root.right)

    # 中序遍历
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.elem)
        self.inorder(root.right)

    # 后序遍历
    def postorder(self, root):
        if root == None:
            return
        self.inorder(root.left)

        self.inorder(root.right)
        print(root.elem)

    # def search(self, elem):

'''


'''

if __name__ == '__main__':

    t = Tree()
    t.add(10)
    t.add(20)
    t.add(30)
    # t.travel()
    t.preorder(t.root)
    # t.search(10)
    # print(a.item)