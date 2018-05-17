def Seqence(n, residue = 0, prev = 1, A = ''):
    if n:
        for i in range(prev, k + 1):
            if residue >= prev and not (n == 1 and residue != i):
                Seqence(n - 1, residue - i, i, A + str(i) + ' ')

    else:
        print(A)

k, n = map(int, input().split())
Seqence(n, k)