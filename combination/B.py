def Seqence(n, A = ''):
    if not n:
        print(A)
    else:
        for i in range(k):
            Seqence(n - 1, A + str(i) + ' ')
n, k = map(int, input().split())
Seqence(n)