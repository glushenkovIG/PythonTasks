ind, n = input().split('~')
ans = 0
len = 0
for elem in n:
    ans = ans * 2 + int(elem)
    len = len * 2 + 1
if ind == '1' and n == '1':
    print(-1)
elif ind == '1':
    print(((~ans) ^ len))
else:   
    print(ans)
     
