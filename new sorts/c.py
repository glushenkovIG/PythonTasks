n = int(input())
A = list(map(int, input().split()))
x = n // 2
B = [A[0]]
for i in range(1, x + 1):
    B.extend([A[-i], A[i]])
print(' '.join(map(str, B[:len(A)])))