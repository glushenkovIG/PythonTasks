prot, fat, carb = list(map(float, input().split()))
prot_ = 0
fat_ = 0
carb_ = 0
n = int(input())
for i in range(n):
    a, b, c, count = list(map(float, input().split()))
    prot_ += a * count
    fat_ += b * count
    carb_ += c * count
if (prot_ >= prot - 0.000001) and (fat_ >= fat - 0.000001) and (carb_ >= carb - 0.000001):
    print('YES')
else:
    print(п'NO')
