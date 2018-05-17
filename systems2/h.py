x, y = list(map(float, input().split()))
i = 1
sum_ = x
while sum_ < y - 0.0000001:
    x *= 1.7
    sum_ += x
    i += 1
print(i)