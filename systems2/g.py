x, y = list(map(float, input().split()))
i = 1
while x < y - 0.0000001:
    x *= 1.7
    i += 1
print(i)