def foo():
    for i in range(0, 10):
        yield i


print(foo())
print(type(foo()))

for n in foo():
    print(n)


def func():
    for c in 'hello world':
        c += '-'
        yield c


text = list(func())
print(text)
