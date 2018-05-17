n = int(input())
A = list(map(int, input().split()))
i = 0
while A[i:] != A[i:][::-1]:
    i += 1
print(i)
print(' '.join(map(str, A[:i][::-1])))