input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline().rstrip()
best_res = 0
second_res = 0
count_second = 1
while len(a) > 0:
    [name, thirname, form, score] = a.split(' ')
    form = int(form) - 9
    score = int(score)
    if best_res < score:
        second_res = best_res
        best_res = score
        count_second = 1
    elif best_res > second_res > score:
        second_res = score
        count_res = 1
    elif second_res == score:
        count_second += 1
    a = input.readline().rstrip()
print(second_res, count_second, file = output)
input.close()
output.close()
