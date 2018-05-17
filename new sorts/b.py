A = []
n = int(input())
amount = 0 
for i in range(n):
    In, Of = list(map(int, input().split()))
    A.append([In, Of])
t = int(input())
for elem in A:
    if elem[0] <= t and elem[1] >= t:
        amount += 1
print(amount)
