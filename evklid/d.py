def IsPrime(n):
    if n % 2 != 0:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return False

a = int(input())
A = []
while not IsPrime(a):
    if a % 2 != 0:
        for i in range(3, int(a ** 0.5) + 1, 2):
            if a % i == 0 and IsPrime(i):
                A.append(i)
                a = a // i
                pass
    else:
        A.append(2)
        a = a // 2
A.append(a)
print(' '.join(map(str, sorted(A))))
            
