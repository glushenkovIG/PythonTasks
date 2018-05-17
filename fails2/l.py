input = open('input.txt', 'r')
output = open('output.txt', 'w')
strip1 = input.readline().rstrip()
strip2 = input.readline().rstrip()
common = ''
first = [0 for i in range(10)]
second = [0 for i in range(10)]
for i in range(len(strip1)):
        first[9 - int(strip1[i])] += 1
for i in range(len(strip2)):
        second[9 - int(strip2[i])] += 1
for i in range(10):
        common += min(first[i], second[i]) * str(9 - i)
if common == '':
        output.write(str(-1))
elif common == '0' * len(common):
        output.write('0')
else:
        output.write(str(common))
input.close()
output.close()