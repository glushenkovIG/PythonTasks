A = list(map(int, input().split()))
count = 0
for i in range(9):
    if A[i] == 2 and A[i + 1] != 2:
        A[i] = 0
        count += 1
print(sum(A) // (10 - count))