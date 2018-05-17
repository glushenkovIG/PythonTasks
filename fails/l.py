input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readlines()
a.sort()
for i in range(len(a)):
    [name, surname, school, score] = a[i].split()
    print(name, surname, score, file = output)
input.close()
output.close()