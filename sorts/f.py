def InsertionSort(A):
    num_1 = 0
    for i in range(1, len(A)):
        num_1 = i - 1
        while A[num_1] > A[i] and num_1 != -1:
            num_1 -= 1
        num_2 = i
        elem = A[i]
        while num_1 != num_2:
            A[num_2] = A[num_2 - 1]
            num_2 -= 1
        A[num_1 + 1] = elem
    return A


A = list(map(int, input().split()))
print(' '.join(map(str, InsertionSort(A))))
        