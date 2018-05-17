n, m = list(map(int, input().split()))
A = [ [m * i + j + int(i % 2) * (m - 1) - int(i % 2) * 2 * j for j in range(m)] for i in range(n)]
for elem in A:
    print(' '.join(map(str, elem)))