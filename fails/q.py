input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline()
schools = [[0, 0] for i in range(1000)]
count = 0
while len(a) != 0:
    name, surname, school, score = a.split()
    school = int(school)
    schools[school][0] -= 1
    if schools[school][1] != school:
        schools[school][1] = school
        count += 1
    a = input.readline()
schools.sort()
for i in range(count):
    print(schools[i][1], end = ' ', file = output)
input.close()
output.close()