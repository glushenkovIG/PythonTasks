n = int(input())
A = list(map(int, input().split()))
count_5 = 0
count = 0
for elem in A:
    if elem == 5:
        count_5 += 1
    else:
        if count_5 > elem // 5 - 1:
            count_5 -= elem // 5 - 1
        else:
            count += elem // 5 - count_5 - 1
            count_5 = 0
if count > 0:
    print(count)
else:
    print(0)