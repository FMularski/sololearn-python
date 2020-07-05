empty_tuple = ()
colors = ('red', 'green', 'blue')
seasons = 'spring', 'summer', 'autumn', 'winter'
print(empty_tuple, colors, seasons)


numbers = tuple(x for x in range(0, 10))
print(numbers[3:7])
print(numbers[::2])
print(numbers[5:-1])
print(numbers[::-1])

if all(type(n) == int for n in numbers):
    print('all numbers are int')

if any(n == 6 for n in numbers):
    print('there is a 6 in the numbers')


