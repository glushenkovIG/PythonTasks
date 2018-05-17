def bin(n):
    if n == 0:
        return 
    else:
        n = n >> 1
        bin(n)
        if n != 0:
            print(n ^ ((n >> 1) << 1), end = '')
        
        
n = int(input())
ans = bin((n << 1) | 1)
