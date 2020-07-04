try:
    result = 1 / 0
    print(result)
except ZeroDivisionError:
    print('cannot divide by zero')

print('*' * 25)

try:
    int('abc')
    print(1 / 0)    # this will not be executed
except ValueError:
    print('invalid value')
except ZeroDivisionError:
    print('zero')

print('*' * 25)

try:
    invalid_file = open('non_existing_file', 'rb')
except:
    print('an error occurred')

print('*' * 25)

try:
    a = 5
    print(a)
    a = 1 / 0
    print(a)
    a = 1
except ZeroDivisionError:
    print('zero before finally')
finally:
    print('finally: ', a)

print('*' * 25)

assert 2 + 2 == 4
# assert 2 + 2 == 5           # try/catch/finally --> to control user     assert --> to control programmer

path = 'files_for_testing/'

file1 = open(path + '1.txt')
print(file1.read())
file1.close()
print('*' * 25)

file2 = open(path + '2.txt')
print(file2.read(5))
file2.close()
print('*' * 25)

file3 = open(path + '3.txt')

for line in file3.readlines():
    print(line)

file3.close()
print('*' * 25)

file4 = open(path + '4.txt', 'w')
file4.write('this is written by the program\n')
file4.close()
print('*' * 25)

file5 = open(path + '5.txt', 'w')
_bytes = file5.write('this is written by the program\n')
print('bytes written:', _bytes)
file5.close()
print('*' * 25)

try:
    file6 = open(path + '6.txt')
    print(file6.read())
finally:
    file6.close()
print('*' * 25)

with open(path + '7.txt', 'w') as file7:
    file7.write('open files by using with')







