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
    else:
        return False
    
        
fin = open('input.txt')
fout = open('output.txt', 'w')
n = int(fin.readline())
pedigree = dict()
for i in range(n - 1):
    child, parent = fin.readline().split()
    if parent in pedigree:
        pedigree[parent] += [child]
    else:
        pedigree[parent] = [child]
s = fin.readline()
while s:
    child, parent = s.split()
    if IsPedigree(False, child, parent, pedigree):
        print(2)
    elif IsPedigree(False, parent, child, pedigree):
        print(1)
    else:
        print(0)
    s = fin.readline()
fin.close()
fout.close()
    