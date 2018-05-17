n = int(input())
A = list(map(int, input().split()))
way = len(A)
for i in range(n):
    if A[i] < 0:
        for h in range(i + 1, n):
            if -A[i] == A[h] and way > h - i:
                way = h - i
if way != len(A):
    print(way)
else:
    print(0)