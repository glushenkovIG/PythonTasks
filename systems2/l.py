max_ = 0.0
ans = 1.0
while ans * 2 != ans * 2 + 1:
    ans *= 2
    max_ = 2 * ans
print(max_)
