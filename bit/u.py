A = input()
h = 0
for elem in A:
    h = (h << 4) + ord(elem)
    h = h ^ ((h >> 32) << 32)
    if h > 0b1111111111111111111111111111:
        h = h ^ ((h & 0b11110000000000000000000000000000) >> 24)
        h = h & 0b1111111111111111111111111111
print(h)