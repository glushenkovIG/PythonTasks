def Seqence(n, last = 1, A = ''):
    if not n:
        print(A)
    else:
        for i in range(n, last - 1, -1):
            Seqence(n - i, i, A + str(i) + ' ')

n = int(input())
Seqence(n)