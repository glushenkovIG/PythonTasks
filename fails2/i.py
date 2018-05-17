input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline(1)
letters = 0
words = 0
lines = 0
previous = ''
while a != '':
        if 'a' <= a <= 'z' or 'A' <= a <= 'Z':
                letters += 1
        elif ('a' <= previous <= 'z' or 'A' <= previous <= 'Z') and (a < 'A' or 'Z' < a < 'a' or a > 'z'):
                words += 1
        if a == '\n':
                lines += 1
        previous = a
        a = input.readline(1)
print('Input file contains:', file = output)
print(letters, 'letters', file = output)
print(words, 'words', file = output)
print(lines, 'lines', end = '', file = output)
input.close()
output.close()
