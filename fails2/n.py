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
sum_ = 0
while a != '':
    while parties[i][1] != a:
        i += 1
    parties[i][0] += 1
    sum_ += 1
    i = 0
    a = input.readline().rstrip()
for i in range(len(parties)):
    if parties[i][0] / sum_ * 100 > 7:
        output.write(str(parties[i][1]) + '\n')
input.close()
output.close()