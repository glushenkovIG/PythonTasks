def IsPedigree(answer, child, parent, pedigree):
    if parent in pedigree:
        if child in pedigree[parent]:
            answer = True
            return answer
        else:
            for new_parent in pedigree[parent]:
                answer = IsPedigree(answer, child, new_parent, pedigree)
                if answer:
                    return True     
    return False   
        
        
input = open('input.txt')
output = open('output.txt', 'w')      
n = int(input.readline())
pedigree = dict()
for i in range(n - 1):
    child, parent = input.readline().split()
    if parent in pedigree:
        pedigree[parent] += [child]
    else:
        pedigree[parent] = [child]
a = input.readline()
while a:
    men1, men2 = a.split()
    if IsPedigree(False, men1, men2, pedigree):
        output.write('2' + '\n')
    elif IsPedigree(False, men2, men1, pedigree):
        output.write('1' + '\n')
    else:
        output.write('0' + '\n')
    a = input.readline()
input.close()
output.close()