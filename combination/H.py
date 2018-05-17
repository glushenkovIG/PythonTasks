def Seqence(n, previous = 0, A = ''):
    if n:
        for i in range(previous + 1, k + 1):
            Seqence(n - 1, i, A + str(i) + ' ')
    else:
        print(A)

n, k = map(int, input().split())
Seqence(n)