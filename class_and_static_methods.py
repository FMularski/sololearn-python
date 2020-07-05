class A:
    nice_var = 100

    def foo(self):
        print('here method')

    @classmethod
    def foo_class(cls):
        print('here class method')

    @staticmethod
    def foo_static():
        print('here static method')


a = A()
a.foo()
a.foo_class()
a.foo_static()