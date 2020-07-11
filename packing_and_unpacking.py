def foo(a1, *b1):
    print(a1)
    print(b1)


foo(1, 2, 3, 4, 5, 6, 7)


x = 1, 2, 3
print(x)


t, y, u = (1, 2, 3)
print(t, y, u)


a, *b = 1, 2, 3
print(a, b)


aa, *bb, cc, dd = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(aa, bb, cc, dd)


def func(**kwargs):
    print(kwargs)
    print(kwargs['q'])
    print(kwargs['r'])


func(q=1, r=2)

