def Supermarket(a, A):
    A.sort(reverse = True)
    summ = 0
    for i in range(0, len(A) - 1, 3):
        summ += A[i] + A[i + 1]
    return summ
        
a = int(input())
A = list(map(int, input().split()))
if len(A) == 1:
    print(A[0])
else:
    print(Supermarket(a, A))