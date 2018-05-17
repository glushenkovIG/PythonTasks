def Seqence(n, k, A = ''):
    if not n:
        print(A)
    else:
        for i in range(k + 1):
            Seqence(n - 1, k, A + str(i) + ' ')
n, k = map(int, input().split())
Seqence(n, k)