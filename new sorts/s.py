def Bubble(F):
    g = 0
    while g < len(F) - 1:
        if F[g][0] == F[g + 1][0] and F[g][1] > F[g + 1][1]:
            F[g], F[g + 1] = F[g + 1], F[g]
            g -= 2
        g += 1
    return F


n = int(input())
Points = [0] * (n + 1)
A = []
for i in range((n * (n - 1)) // 2):
    A.append(list(map(int, input().split())))
for elem in A:
    if elem[2] == elem[3]: 
        Points[elem[0]] += 1
        Points[elem[1]] += 1
    elif elem[2] > elem[3]:
        Points[elem[0]] += 3
    else:
        Points[elem[1]] += 3
F = []
for h in range(n):
    max_ = max(Points)
    ind = 0
    while Points[ind] != max_:
        ind += 1
    F.append((max_, ind))
    Points[ind] = 0
F.sort(reverse = True)
F = Bubble(F)
for i in range(len(F)):
    print(' '.join(map(str, F[i][::-1])))    