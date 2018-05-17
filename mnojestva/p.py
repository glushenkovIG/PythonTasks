input = open('input.txt', 'r')
output = open('output.txt', 'w')
text = dict()
a = input.read().split()
for elem in a:
    if elem not in text:
        text[elem] = -1
    else:
        text[elem] -= 1
A = [[text[elem], elem] for elem in text]
A.sort()
print('\n'.join([elem[-1] for elem in A]))
input.close()
output.close()