input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline()
peoples = []
while len(a) != 0:
    surname, name, form, score = a.split()
    peoples.append([-int(score), surname, name])
    a = input.readline()
peoples.sort()
for i in range(len(peoples)):
    output.write(str(peoples[i][1]) + ' ' + str(peoples[i][2]) + ' ' + str(-peoples[i][0]) + '\n')
input.close()
output.close()