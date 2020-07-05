class A:
    static_var = 1

    def __init__(self, x):
        self.x = x

    def foo(self):
        print('123')

    @staticmethod
    def increase_static_var_by_one():
        A.static_var += 1


class B(A):
    def foo(self):
        super().foo()
        print('abc')


a1 = A(10)
a2 = A(10)

print(A.static_var)
print(a1.static_var)
print(a2.static_var)
A.increase_static_var_by_one()
print(A.static_var)
print(a1.static_var)
print(a2.static_var)
a1.increase_static_var_by_one()
print(A.static_var)
print(a1.static_var)
print(a2.static_var)

a1.x += 1
print(a1.x)

b1 = B(5)
print(B.static_var)
A.increase_static_var_by_one()
print(B.static_var)

b1.foo()




