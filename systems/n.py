a = list(map(str, input()))[::-1]
n = int(input())
a.append(0)
N = -1
if n > 10:
    a[0] = ord(a[0]) + 11 - ord('A')
    i = 1
    while ord(a[i]) - ord('A') + 10 >= n - 1:
        if 'A' <= a[i] <= 'Z':
            a[i] = ord(a[i]) - ord('A') + 10
        i += 1
    N = i
    a[:N] = list(map(int, a[:N]))
    if '0' <= a[N] <= '9':
        a[N] = int(a[N])
    else:
        a[N] = ord(a[N]) - ord('A') + 10
else:
    a = list(map(int, a))
    a[0] += 1
i = 0
while i < N:
    a[i + 1] += a[i] // n
    a[i] %= n
    if a[i] >= 10:
        a[i] = chr(ord('A') + a[i] - 10)
    i += 1
if a[N] >= 10:
    a[N] = chr(ord('A') + a[i] - 10)
a = a[::-1]
if a[0] != 0:
    print(''.join(list(map(str, a))))
else:
    print(''.join(list(map(str, a[1:]))))
    