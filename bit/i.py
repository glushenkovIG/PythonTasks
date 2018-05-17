input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline()
ans = 0
while a:
    ans = ans ^ int(a)
    a = input.readline()
output.write(str(ans))
input.close()
output.close()
