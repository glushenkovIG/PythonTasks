def Seqence(n, count = 0, A = ''):
    if n and count <= k:
        Seqence(n - 1, count, A + '0')
        if A == '' or A[-1] != '1':
            Seqence(n - 1, count + 1, A + '1')
    elif count == k:
        print(' '.join(A))

n, k = map(int, input().split())
Seqence(n)