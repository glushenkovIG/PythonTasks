a = float(input())
b = float(input())
c = float(input())
if (a + b - c < 0.00000001) and (a + b - c > - 0.00000001):
    print('YES')
else:
    print('NO')