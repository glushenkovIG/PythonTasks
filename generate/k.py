n, m = list(map(int, input().split()))
A = [ [(j - i) % 3 for j in range(m)] for i in range(n)]
for elem in A:
    print(' '.join(map(str, elem)))