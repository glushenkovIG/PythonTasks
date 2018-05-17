input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readlines()
i = len(a) - 1
while i != -1:
    print(a[i][:-2], file = output)
    i -= 1
input.close()
output.close()