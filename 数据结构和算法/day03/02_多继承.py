class A:
    def run(self):
        print('a')

class B(A):
    # def run(self):
    #     print('b')
    pass

class C(A):
    def run(self):
        print('c')

class D(B, C):
    pass

d = D()
d.run()