fin = open('input.txt')
fout = open('output.txt', 'w')
amount = int(fin.readline())
Stations = []
man = fin.readline()
while man:
    man = man.split()
    Stations.append([int(man[-2]), int(man[-1])])
    man = fin.readline()
Max_stations = [0 for i in range(amount)]
for i in range(len(Stations)):
    for j in range(Stations[i][0], Stations[i][1]):
        Max_stations[j] += 1
answer = ''
Max = 0
for i in range(amount):
    if Max_stations[i] > Max:
        Max = Max_stations[i]
        answer = str(i) + '-' + str(i + 1) + '\n'
    elif Max_stations[i] == Max:
        answer += str(i) + '-' + str(i + 1) + '\n'
fout.write(answer)
fin.close()
fout.close()
