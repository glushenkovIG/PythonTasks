def string(A):
    B = [1]
    for i in range(len(A) - 1):
        B.append(A[i] + A[i + 1])
    B.append(1)
    return B


A = [1, 1]
n = int(input())
print(1)
for i in range(n):
    print(' '.join(map(str, A)))
    A = string(A)