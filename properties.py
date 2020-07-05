class A:
    @property
    def foo(self):
        print('hello')

    @foo.setter
    def foo(self, value):
        print('set value now')

    @foo.getter
    def foo(self):
        print('get value now')


a = A()
a.foo = 10
a.foo