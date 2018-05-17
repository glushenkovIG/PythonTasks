input = open('input.txt', 'r')
output = open('output.txt', 'w')
text = dict()
a = input.read().split()
for elem in a:
    if elem not in text:
        text[elem] = 0
    else:
        text[elem] += 1
    print(text[elem], end = ' ', file = output)
input.close()
output.close()