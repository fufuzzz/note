class A:
    _instance  = None
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)

        return cls._instance

a = A()
b = A()


