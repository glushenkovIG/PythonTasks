input = open('input.txt', 'r')
output = open('output.txt', 'w')
names = dict()
a = input.readline().rstrip().split()
while a != []:
    name, thing, count = a[0], a[1], int(a[2])
    things = dict()
    if name in names:
        if thing in names[name]:
            names[name][thing] += count
        else:
            names[name][thing] = count
    else:
        things[thing] = count
        names[name] = things
    a = input.readline().rstrip().split()
NAMES = sorted([elem for elem in names])
for elem in NAMES:
    output.write(elem + ':' + '\n')
    THINGS = sorted([elem for elem in names[elem]])
    for elem1 in THINGS:
        output.write(elem1 + ' ' + str(names[elem][elem1]) + '\n')
input.close()
output.close()