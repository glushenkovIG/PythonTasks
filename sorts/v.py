def Intersection(A, B):
    m = 0
    FINAL = []
    h = 0
    while len(A) > m:
        if h < len(B) and A[m] >= B[h]:
            FINAL.append(B[h])
            h += 1 
        else:
            FINAL.append(A[m])
            m += 1
    if h < len(B):
        FINAL.extend(B[h:])
    C = []
    for i in range(len(FINAL) - 1):
        if FINAL[i] == FINAL[i + 1]:
            C.append(FINAL[i])
    return C


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(' '.join(map(str, Intersection(A, B))))