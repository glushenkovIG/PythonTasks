input = open('input.txt', 'r')
output = open('output.txt', 'w')
for i in range(366):
    a = input.readline()
    print(i + 1 == int(a))
input.close()
output.close()
    