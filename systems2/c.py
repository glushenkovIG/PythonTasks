def bin2int(a):
    ind = len(a) - 1
    ans = 0
    i = 0
    while i < len(a):
        if a[i] == '.':
            ind = i
        else:
            ans = ans * 2 + int(a[i])
        i += 1
    return ans / (1 << (len(a) - ind - 1))


a, b = input().split('.')
k = len(b)
for i in range(len(b)):
    if b[i] == '(':
        k = i
m = len(b) - k - 2
ans = a + '.' + b[:k]
x = bin2int(b[k + 1:-1]) / (2 ** (m + k) - 2 ** k)
print(x + bin2int(ans))

