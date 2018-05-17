n = int(input())
A = [ [int(abs(-j - i - 3) % 4 == 0) for j in range(n)] for i in range(n)]
for elem in A:
    print(' '.join(map(str, elem)))