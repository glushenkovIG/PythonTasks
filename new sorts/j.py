n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
bus = []
i = 0
for elem in A:
    bus.append([elem, i])
    i += 1
bus.sort(reverse = True)
num_bus = 0
index = []
if sum(A) < n:
    print(-1)
else:
    for elem in bus:
        if n > 0:
            n -= elem[0]
            index.append(elem[1] + 1)
            num_bus += 1
    print(num_bus)
    index.sort()
    print(' '.join(map(str, index)))