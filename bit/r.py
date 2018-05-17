A = input()
h = 0
for elem in A:
    h = h ^ ((h >> 16) << 16)
    h = (h >> 1) | ((h & 1) << 15)
    h += ord(elem)
print(h)