def Chisla(A):
    max_ = 0
    elem_1 = A[0]
    elem_2 = A[1]
    for i in range(len(A) - 1):
        for h in range(i + 1, len(A)):
            if A[i] * A[h] > max_:
                max_ = A[i] * A[h]
                elem_1 = A[i]
                elem_2 = A[h]
    return min(elem_1, elem_2), max(elem_1, elem_2)

A = list(map(int, input().split()))
print(' '.join(list(map(str, Chisla(A)))))
