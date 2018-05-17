def Seqence(count_op = 0, count_cl = 0, op = 0, cl = 0, A = ''):
    if op == n and cl == op:
        print(A)
    else:
        if count_op < k and op < n and (op >= cl or op == 0):
            Seqence(count_op + 1, 0, op + 1, cl, A + '(')
        if count_cl < k and cl < n and op != 0:
            Seqence(0, count_cl + 1, op, cl + 1, A + ')')
n, k = map(int, input().split())
Seqence()