A = list(map(int, input().split()))
n = int(input())
A = A[n:23 - n - (23 - n) % 7]
min_sum = sum(A[:7])
for i in range(0, len(A), 7):
    sum_ = sum(A[i:i + 7])
    if sum_ < min_sum:
        min_sum = sum_
print(min_sum)