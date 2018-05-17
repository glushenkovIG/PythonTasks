a = list(map(str, input()[::-1]))
b = list(map(str, input()[::-1]))
if len(a) < len(b):
    a, b = b, a
a.append('0')
b.append('0')
for i in range(len(a)):
    if 'A' <= a[i] <= 'Z':
        a[i] = ord(a[i]) - ord('A') + 10
for i in range(len(b)):
    if 'A' <= b[i] <= 'Z':
        b[i] = ord(b[i]) - ord('A') + 10
    a[i], b[i] = int(a[i]), int(b[i])
    a[i] += b[i]
for i in range(len(b)):
    if a[i] >= 16:
        a[i + 1] = int(a[i + 1])
        a[i + 1] += a[i] // 16
    a[i] %= 16
    if a[i] >= 10:
        a[i] = chr(ord('A') + a[i] - 10)
i = 0
a = a[::-1]
while a[i] == '0' or a[i] == 0 and i < len(a) - 1:
    a[i] = ''
    i += 1
print(''.join(map(str, a[i:])))
