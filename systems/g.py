n = int(input())
a = list(map(str, input()))
k = int(input())
for i in range(len(a)):
    if 'A' <= a[i] <= 'Z':
        a[i] = ord(a[i]) - ord('A') + 10
a = list(map(int, a))
int_a = 0
for i in range(len(a)):
    int_a = int_a * n + a[i] % n
ans = []
if int_a != 0:
    while int_a != 0:
        r = int_a % k
        if r > 10:
            r = chr(r - 10 + ord('A'))
        ans.append(r)
        int_a //= k
    print(''.join(list(map(str, ans)))[::-1])
else:
    print('0')