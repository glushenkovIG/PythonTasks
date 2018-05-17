def DEEP(pedigree, mans, count, parent):
    if parent in pedigree:
        for child in pedigree[parent]:
            mans[child] = count + 1
            DEEP(pedigree, mans, count + 1, child)
        
        
n = int(input())
mans = dict()
pedigree = dict()
CHILDREN = set()
for i in range(n - 1):
    child, parent = input().split()
    if parent in pedigree:
        pedigree[parent].append(child)
    else:
        pedigree[parent] = [child]
    CHILDREN.add(child)
    if parent not in mans:
        mans[parent] = 0
    if child not in mans:
        mans[child] = 0
first_parent = list(set(mans) - CHILDREN)[0]
DEEP(pedigree, mans, 0, first_parent)
for men in sorted(mans):
    print(men, mans[men])