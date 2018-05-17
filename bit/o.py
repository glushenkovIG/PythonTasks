cheater = 0b101010101010101010101010101010101
a = int(input())
print((((cheater << 1) & a) >> 1) | ((cheater & a) << 1))