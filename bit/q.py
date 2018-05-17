a = int(input())
b = a
t = a
if a == 0:
    print('0~0')
elif a == -1:
    print('1~1')
elif a < -1:
    b = -a - 1
    print('1~', end = '')
    a = ~a 
else:
    print('0~', end = '')
len = 0
while b > 0:
    b = b >> 1
    len += 1
if t < 0:
    a = ((~a >> len) << len) ^ ~a
for i in range(len - 1, -1, -1):
    print(((((1 << i) & a)) >> i), end = '')