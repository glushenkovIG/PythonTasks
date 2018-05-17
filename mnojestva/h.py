input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = int(input.readline().rstrip())
didgits = input.readline().split()
variation = set([str(i + 1) for i in range(a)])
while didgits[0] != 'HELP':
    if len(set(didgits) & variation) > len(variation - set(didgits)):
        variation &= set(didgits)
        print('YES', file = output)
    else:
        variation -= set(didgits)
        print('NO', file = output)
    didgits = input.readline().split()
print(' '.join(list(map(str, (sorted(map(int, variation)))))), file = output)
input.close()
output.close()