def Seqence(n, previous = 0, A = ''):
    if not n:
        print(A)
    else:
        if n == previous:
            Seqence(0, 0, A + ' '.join([str(i) for i in range(previous, 0, -1)]))
        elif n < previous:
            for i in range(previous, 0, -1):
                Seqence(n - 1, i - 1, A + str(i) + ' ')

n, k = map(int, input().split())
Seqence(n, k)