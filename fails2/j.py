input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = list(map(str, input.readline().rstrip()))
num = 1
while len(a) != 0:
    for i in range(len(a)):
        x = ord('z') - ord('a')
        if 'a' <= a[i] <= 'z':
            a[i] = chr((ord(a[i]) - ord('a') + num) % (x + 1) + ord('a'))
        elif 'A' <= a[i] <= 'Z':
            a[i] = chr((ord(a[i]) - ord('A') + num) % (x + 1) + ord('A'))
        else:
            a[i] = a[i]
    num += 1
    print(''.join(a), file = output)
    a = list(map(str, input.readline().rstrip()))
input.close()
output.close()