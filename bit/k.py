a, b = map(int, input().split())
ans = (a << 4) + (a << 1) + (b >> 4)
print(ans ^ ((ans >> 5) << 5))