a = input()
A = 1
B = 0
for elem in a:
    A += ord(elem)
    B += A 
A %= 65521
B %= 65521
print((B << 16) + A)