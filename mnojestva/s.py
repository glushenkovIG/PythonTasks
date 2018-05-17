input = open('input.txt', 'r')
output = open('output.txt', 'w')
words = dict()
n = int(input.readline())
len_words = 0
for i in range(n):
    a = input.readline().rstrip().split(' - ')
    A = a[1].split(', ')
    for elem in A:
        if elem in words:
            words[elem] += [a[0]]
        else:
            words[elem] = [a[0]]
            len_words += 1
output.write(str(len_words) + '\n')
for elem in sorted(words):
    output.write(elem + ' - ' + ', '.join(sorted(words[elem])) + '\n')
input.close()
output.close()