def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = list(map(int, input().split()))
print(gcd(a, b))