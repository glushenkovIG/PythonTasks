input = open("input.txt", 'r')
output = open('output.txt', 'w')
a = input.read()
b, c = a.split(' ')
print(int(b) + int(c), file = output)
input.close()
output.close()