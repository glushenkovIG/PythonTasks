input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline()
sum_schools = [0 for i in range(1000)]
midl_schools = [[0, 0] for i in range(1000)]
sum_peop_schools = [0 for i in range(1000)]
while a != '':
    name, surname, school, score = a.split()
    school = int(school)
    score = int(score)
    sum_schools[school] += score
    sum_peop_schools[school] += 1
    a = input.readline()
for i in range(1000):
    if sum_peop_schools[i] != 0:
        midl_schools[i][0] = sum_schools[i] / sum_peop_schools[i]
        midl_schools[i][1] = -i
midl_schools.sort(reverse = True)
for i in range(1000):
    if midl_schools[i][0] != 0:
        print(-midl_schools[i][1], end = ' ', file = output)
input.close()
output.close()
