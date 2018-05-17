k, n = list(map(int, input().split()))
A = []
for i in range(k):
    A.append(list(map(int, input().split())))
for h in range(n):    
    min_ = A[0]
    MIN = []
    for g in range(k):
        MIN.append(A[g][h])
    print(min(MIN), end = ' ')