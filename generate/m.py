n, m = list(map(int, input().split()))
A = [ [abs(int(i % 2 == j % 2 and i % 2 == 1) - 1) for j in range(m)] for i in range(n)]
for elem in A:
    print(' '.join(map(str, elem)))