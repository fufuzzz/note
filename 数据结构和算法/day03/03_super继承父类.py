class A:
    def run(self):
        print('a')

class B(A):
    def run(self):
        super(B, self).run()
        print('b')
    # pass

class C(A):
    def run(self):
        super(C, self).run()
        print('c')

class D(B, C):


    def run(self):
        super(D, self).run()
        print('d')

d = D()
d.run()

print(D.__mro__)