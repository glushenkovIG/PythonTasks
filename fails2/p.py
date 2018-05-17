input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline().rstrip()
peop = [a]
count = [0] * 20
max_ = ''
second = ''
count_max = 0
count_second = 0
all_ = 0
while a != '':
    if a in peop:
        count[peop.index(a)] += 1
    else:
        peop.append(a)
        count[len(peop) - 1] += 1
    a = input.readline().rstrip()
    all_ += 1
for i in range(len(peop)):
    if count_max < count[i]:
        second = max_
        max_ = peop[i]
        count_second = count_max
        count_max = count[i]
    elif count_second < count[i]:
        second = peop[i]
        count_second = count[i]
output.write(max_ + '\n')
if all_ / 2 >= count_max:
    output.write(second)
input.close()
output.close()
