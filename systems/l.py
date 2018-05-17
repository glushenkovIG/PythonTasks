a = int(input())
ans = ''
while a != 0:
    residue = a % 3
    a //= 3
    if residue == 2:
        ans += '$'
        a += 1
    else:
        ans += str(residue)
print(ans[::-1])