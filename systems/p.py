a = list(map(str, input()))[::-1]
a.append('0')
for i in range(len(a)):
    if a[i] == '$':
        a[i] = '-1'
a[0] = str(int(a[0]) + 1)
for i in range(len(a)):
    if a[i] == '-1':
        a[i] = '$'
    if a[i] == '2':
        a[i] = '$'
        a[i + 1] = str(int(a[i + 1]) + 1)
if len(a) != 1 and a[-1] == '0':
    a = a[:-1]
if len(a) != 1 and a[-1] == '0':
    a = a[:-1]
print(''.join(list(map(str, a))[::-1]))
        
