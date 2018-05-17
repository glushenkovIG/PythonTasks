def Fraction(n):
    A = []
    for i in range(n):
        a, b = list(map(int, input().split('/')))
        A.append((a, b)) 
    for i in range(n):
        for h in range(n - 1, 0, -1):
            if A[h][0] * A[h - 1][1] < A[h][1] * A[h - 1][0]:
                A[h], A[h - 1] = A[h - 1], A[h]
            elif A[h][0] * A[h - 1][1] == A[h][1] * A[h - 1][0]:
                if A[h][1] < A[h - 1][1]:
                    A[h], A[h - 1] = A[h - 1], A[h]
    for i in range(n):
        print(A[i][0], '/', A[i][1], sep = '')
     
                    
n = int(input())
Fraction(n)