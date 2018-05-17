def Seqence(n, count = 0, A = ''):
    if n:
        if n >= k - count:
            Seqence(n - 1, count, A + '0')
        if n > k - count:
            if count < k:
                Seqence(n - 1, count + 1, A + '1')
    else:
        print(' '.join(A))

n, k = map(int, input().split())
Seqence(n)