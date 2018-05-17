input = open('input.txt', 'r')
output = open('output.txt', 'w')
words = dict()
a = input.readline().split()
while len(a) > 0:
    if len(a) == 1:
        output.write(words[a[0]] + '\n')
    else:
        words[a[0]] = a[1] 
        words[a[1]] = a[0]
    a = input.readline().split()
input.close()
output.close()