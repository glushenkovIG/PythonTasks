n = int(input())
A = [ [int(j == i or j == n - i - 1) for j in range(n)] for i in range(n)]
for elem in A:
    print(' '.join(map(str, elem)))