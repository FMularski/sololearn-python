class A:
    __static = 10

    def __init__(self):
        self.a = 1
        self._a = 2
        self.__a = 3


a = A()
print(a.a)

