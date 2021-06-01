class A:
    # _instance  = None
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance == None:
    #         cls._instance = super().__new__(cls)
    #
    #     return cls._instance


    def __del__(self):
        print('abc')


a = A()
b = A()
del b
print('---------')