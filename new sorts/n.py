n, k = list(map(int, input().split()))
A = []
for i in range(k):
    who, whom, how_much = list(map(int, input().split()))
    A.append([who, whom, how_much])
All_arrears = [0] * (n + 1)
for elem in A:
    All_arrears[elem[0]] -= elem[2]
    All_arrears[elem[1]] += elem[2]
print(' '.join(map(str, All_arrears[1:])))
    