def IsPrime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


a = int(input())
i = a // 2
while not(IsPrime(i) and IsPrime(a - i)):
    i -= 1
print(i, a - i)
