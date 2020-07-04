op = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b,
    3: 4,
    False: 3
    }

print(op)
print(op.items())
print(op.keys())
print(op.values())

print(op.get('mul')(3, 3))
print(op.get(False))
print(op.get(True, 'there is no true'))

print('sub' in op)





