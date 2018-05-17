input = open('input.txt', 'r')
output = open('output.txt', 'w')
file = dict()
n = int(input.readline())
for i in range(n):
    a = input.readline().split()
    name_file = a[0]
    operation = a[1:]
    file[name_file] = operation
n = int(input.readline())
for i in range(n):
    a = input.readline().split()
    if (a[0] == 'write' and 'W' in file[a[1]]) or (a[0] == 'read' and 'R' in file[a[1]]) or (a[0] == 'execute' and 'X' in file[a[1]]):
        print('OK', file = output)
    else:
        print('Access denied', file = output)
input.close()
output.close()