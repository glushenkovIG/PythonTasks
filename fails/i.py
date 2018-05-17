input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline().rstrip()
best_res = 0
second_res = 0
count_second = 1
count_best = 1
best = ''
second = ''
while len(a) > 0:
    name, surname, form, score = a.split()
    form = int(form) - 9
    score = int(score)
    if best_res < score:
        second_res = best_res
        best_res = score
        count_second = count_best
        count_best = 1
        second = best
        best = name + ' ' + surname
    elif best_res == score:
        count_best += 1
    elif best_res > score > second_res:
        second_res = score
        count_second = 1
        second = name + ' ' + surname
    elif second_res == score:
        count_second += 1
    a = input.readline().rstrip()
if count_second != 1:
    print(count_second, file = output)
else:
    print(second, file = output)
input.close()
output.close()