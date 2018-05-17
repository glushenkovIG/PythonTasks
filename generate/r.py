n, m = list(map(int, input().split()))
A = [ [abs(int(j % 4 <= 1) + int(i % 4 <= 1) - 1) for j in range(m)] for i in range(n)]
for elem in A:
    print(' '.join(map(str, elem)))