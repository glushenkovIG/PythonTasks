n, m = list(map(int, input().split()))
A = [ [int(j < i) + int(j != i) for j in range(m)] for i in range(n)]
for elem in A:
    print(' '.join(map(str, elem)))