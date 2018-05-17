def plus_min(a):
    for i in range(len(A)):
        for g in range(i, len(A)):
            if A[i] == -A[g]:
                return i, g
    return '0'
            
A = list(map(int, input().split())) 
print(' '.join(map(str, plus_min(A))))