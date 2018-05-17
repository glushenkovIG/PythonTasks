n = int(input())
A = [ [int(j > i) + int(j > n - i - 1) + int(j < i) + int(j < n - i - 1) - 1 * abs(int(j == i and j == n - i - 1) - 1) + int(j > n - 1 - i and j != i) + int(j < i and j != i and j != n - i - 1) + 2 * int(j < i and j != i and j != n - i - 1 and j < n - i - 1) for j in range(n)] for i in range(n)]
for elem in A:
    print(' '.join(map(str, elem)))