a = list(map(str, input()))[::-1]
n = int(input())
if n > 10:
    for i in range(len(a)):
        if 'A' <= a[i] <= 'Z':
            a[i] = ord(a[i]) - ord('A') + 10
a[0] = str(int(a[0]) - 1)
a = list(map(int, a))
i = 0
while i < len(a) - 1 and a[i] == -1:
    a[i + 1] -= 1
    a[i] = n - 1
    if a[i] >= 10:
        a[i] = chr(ord('A') + a[i] - 10)
    i += 1
a = a[::-1]
i = 0
while a[i] == 0 and i < len(a) - 1:
    a[i] = ''
    i += 1
print(''.join(map(str, a[i:])))