class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('lucy', 18)
print(p.__dict__)  # {'name': 'lucy', 'age': 18}
print(Person.__dict__)