import random

n = 10
my_list = [x * random.randint(1, 10) for x in range(1, n + 1)]     # list comprehension syntax
print(my_list)

my_list.sort(reverse=True)
print(my_list)

text = 'hello world'
print(text[0], text[-1])        # the 1st and the last character
text = list(text)
text.sort()
print(text)

while text:
    print(text.pop())

print('text now: ', text)

text = 'python'
text *= 3
print(text)

a = [1, 2]
a += [3, 4]
print(a, len(a), a.index(1))

if 3 in a:
    print('in means contains')


