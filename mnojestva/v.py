input = open('input.txt', 'r')
output = open('output.txt', 'w')
names = dict()
States = dict()
states = dict()
Candidats = dict()
n = int(input.readline())
for i in range(n):
    a = input.readline().split()
    States[a[0]] = int(a[1])
    states[a[0]] = dict()
a = input.readline().split()
while a != []:
    state, name = a[0], a[1]
    names = dict()
    if name in states[state]:
        states[state][name] += 1
    else:
        states[state][name] = 1
    if name not in Candidats:
        Candidats[name] = 0
    a = input.readline().rstrip().split()
for elem in states:
    max_ = 0
    for elem1 in states[elem]:
        if max_ < states[elem][elem1]:
            max_ = states[elem][elem1]
            name_max = elem1
        if max_ == states[elem][elem1] and elem1 < name_max:
            name_max = elem1
    Candidats[name_max] += States[elem]
A = sorted([(-int(Candidats[elem]), elem) for elem in Candidats])
for elem in A:
    output.write(elem[1] + ' ' + str(-elem[0]) + '\n')
input.close()
output.close()