input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline().rstrip()
a = input.readline().rstrip()
parties = []
while a != 'VOTES:':
    parties.append([0, a])
    a = input.readline().rstrip()
i = 0
a = input.readline().rstrip()
while a != '':
    while parties[i][1] != a:
        i += 1
    parties[i][0] -= 1
    i = 0
    a = input.readline().rstrip()
parties.sort()
for i in range(len(parties)):
    output.write(parties[i][1] + '\n')
input.close()
output.close()