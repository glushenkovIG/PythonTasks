input = open('input.txt', 'r')
output = open('output.txt', 'w')
deposits = dict()
a = input.readline().split()
while a != []:
    if a[0] == 'DEPOSIT':
        name, sum = a[1], int(a[2])
        if name in deposits:
            deposits[name] += sum
        else:
            deposits[name] = sum
    elif a[0] == 'WITHDRAW':
        name, sum = a[1], int(a[2])
        if name in deposits:
            deposits[name] -= sum
        else:
            deposits[name] = -sum        
    elif a[0] == 'BALANCE':
        output.write(str(deposits.get(a[1], 'ERROR')) + '\n')
    elif a[0] == 'TRANSFER':
        name1, name2, sum = a[1], a[2], int(a[3])
        if name1 in deposits:
            deposits[name1] -= sum
        else:
            deposits[name1] = -sum
        if name2 in deposits:
            deposits[name2] += sum
        else:
            deposits[name2] = sum
    elif a[0] == 'INCOME':
        p = int(a[1])
        for elem in deposits:
            if deposits[elem] > 0:
                deposits[elem] = int(deposits[elem] * (1 + p / 100))
    a = input.readline().split()   
input.close()
output.close()