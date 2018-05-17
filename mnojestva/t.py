def CountBig(a):
    count = 0
    for i in range(len(a)):
        if 'A' <= a[i] <= 'Z':
                count += 1
    return count


def Small(a):
    a = list(map(str, a))
    for i in range(len(a)):
        if 'A' <= a[i] <= 'Z':
            a[i] = chr(ord(a[i]) + ord('a') - ord('A'))
    return ''.join(a)
input = open('input.txt', 'r')
output = open('output.txt', 'w')
n = int(input.readline())
words = dict()
for i in range(n):
    word = input.readline().rstrip()
    if Small(word) in words:
        words[Small(word)] += [word]
    else:
        words[Small(word)] = [word]
count = 0
line = input.readline().split()
for word in line:
    if CountBig(word) != 1:
        count += 1
    else:
        if Small(word) in words:
            if word not in words[Small(word)]:
                count += 1
output.write(str(count))
input.close()
output.close()