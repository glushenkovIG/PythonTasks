input = open('input.txt')
output = open('output.txt', 'w')
count = int(input.readline())
a = input.readline()
a = a.split()
station = []
distilled = ''
max_peop = 0
peop_on_station = [0] * count
while a != '':
    station.append([int(a[-2]), int(a[-1])])
    a = input.readline()
    a = a.split()
for i in range(len(station)):
    for j in range(station[i][0], station[i][1]):
        peop_on_station[j] += 1
for i in range(count):
    if max_peop < peop_on_station[i]:
        max_peop = peop_on_station[i]
        distilled = str(i) + '-' + str(i + 1) + '\n'
    elif peop_on_station[i] == max_peop:
        distilled += str(i) + '-' + str(i + 1) + '\n'
output.write(distilled)
input.close()
output.close()
