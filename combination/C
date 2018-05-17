def Seqence(n, previous = 0, A = ''):
    if not n:
        print(A)
    else:
        Seqence(n - 1, 0, A + '0 ')
        if previous != 1:
            Seqence(n - 1, 1, A + '1 ')

n = int(input())
Seqence(n)