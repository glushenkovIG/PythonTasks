input = open('input.txt', 'r')
output = open('output.txt', 'w')
candidats = dict()
a = input.readline().split()
while a != []:
    if a[0] in candidats:
        candidats[a[0]] += int(a[1])
    else:
        candidats[a[0]] = int(a[1])
    a = input.readline().split()
sorted_candidats = sorted(list(map(str, candidats)))
for elem in sorted_candidats:
    print(elem, candidats[elem], file = output)
input.close()
output.close()