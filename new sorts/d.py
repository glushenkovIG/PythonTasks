n = int(input())
A = list(map(int, input().split()))
k = int(input())
x = 0
i = 0
max_hour = 0
while i <= n - n % k:
    x = sum(A[i:i + k])
    if x > max_hour:
        max_hour = x
    i += 1
print(max_hour)
        
        
        