input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = int(input.readline().rstrip())
didgits = input.readline().split()
variation = set([str(i + 1) for i in range(a)])
while didgits[0] != 'HELP':
    a = input.readline().rstrip()
    if a == 'NO':
        variation -= set(didgits)
    else:
        variation &= set(didgits)
    didgits = input.readline().split()
output.write(' '.join(list(map(str, sorted(map(int, variation))))))
input.close()
output.close()