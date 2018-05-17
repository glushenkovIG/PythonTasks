def bin_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a == 1 and b == 1:
        return 1
    if not a & 1 and not b & 1:
        return 2 * bin_gcd(a // 2, b // 2)
    if not a & 1 and b & 1:
        return bin_gcd(a // 2, b)
    if a & 1 and not b & 1:
        return bin_gcd(a, b // 2)
    if a & 1 and b & 1 and a >= b:
        return bin_gcd(a - b, b)
    if a & 1 and b & 1 and a < b:
        return bin_gcd(b - a, a)
a, b = int(input()), int(input())
print(bin_gcd(a, b))