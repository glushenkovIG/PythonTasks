h = 14695981039346656037
A = input()
for elem in A:
    h *= 1099511628211
    h = h ^ ord(elem)
    h = h ^ ((h >> 64) << 64)
print(h)