def Seqence(n, residue = 0, prev = 1, A = ''):
    if n:
        for i in range(k, prev - 1, -1):
            if residue >= prev and not (n == 1 and residue != i):
                Seqence(n - 1, residue - i, i, A + str(i) + ' ')

    else:
        print(A[::-1][1:])

k, n = map(int, input().split())
Seqence(n, k)