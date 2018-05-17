n, a, b, c, d = list(map(int, input().split()))
N = []
for i in range(1, n + 1):
    N.append(i)
N = N[:a - 1] + N[a - 1:b][::-1] + N[b:]
N = N[:c - 1] + N[c - 1:d][::-1] + N[d:]
print(' '.join(map(str, N)))
    