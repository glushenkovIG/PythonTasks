n, m = list(map(int, input().split()))
A = [ [((i * m + j) // 2 + 1) * abs(int(j % 2 == 1) + int(i % 2 == 1) - 1) for j in range(m)] for i in range(n)]
for elem in A:
    print(' '.join(map(str, elem)))