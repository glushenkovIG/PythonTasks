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
    return ans / (1 << (len(a) - ind - 1)), ans, (1 << (len(a) - ind - 1))


a, b = input().split('.')
m = len(b)
k = 0
for i in range(len(b)):
    if b[i] == '(':
        m = i
        k = len(b) - m - 2
if k:
    p = (bin2int(b[:m] + b[m + 1:-1])[0] - bin2int(b[:m])[0])
    q = bin2int('1' * k + '0' * m)[0]
    p, q = int(p) + int(bin2int(a)[0] * q), int(q)
else:
    p, q = bin2int(a + '.' + b)[1], bin2int(a + '.' + b)[-1]
print(p, q)
