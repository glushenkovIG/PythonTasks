def Seqence(n, A = ''):
    if not n:
        print(A)
    else:
        Seqence(n - 1, A + '0 ')
        Seqence(n - 1, A + '1 ')
n = int(input())
Seqence(n)