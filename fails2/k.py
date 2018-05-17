input = open('input.txt', 'r')
output = open('output.txt', 'w')
strip1 = input.readline().rstrip()
strip2 = input.readline().rstrip()
yes_no = 'YES'
strip1, strip2 = max(strip1, strip2), min(strip1, strip2)
i = 0
while i != len(strip1) and i <= 127 and yes_no != 'NO':
    if strip1.count(strip1[i]) != strip2.count(strip1[i]):
        yes_no = 'NO'
    i += 1
print(yes_no, file = output)
input.close()
output.close()