def Taxi(A, B):
    A.sort()
    B.sort(reverse = True)
    summ = 0
    for i in range(len(A)):
        summ += A[i] * B[i]
    return summ
        
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(Taxi(A, B))
