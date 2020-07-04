# to int
a = '12'
b = '13'
print(int(a) + int(b))
# c = int('xyz') ValueError


# to float
a = '43.2'
b = '12.01'
print(float(a) + float(b))
# c = float('xyz') ValueError


# to boolean
print(bool(1))
print(bool('abc'))
print(bool(1.23))

print(bool(0))
print(bool(None))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))


# to str
a = 5
b = 3
print(str(a) + str(b))

# to list
a = (1, 2.3, True, 'abc')
a = list(a)
print(a)

# to tuple
a = tuple(a)
print(a)

