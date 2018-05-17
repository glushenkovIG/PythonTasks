def Digits(A):
    if len(A) > 2:
            max_1 = A[0]
            max_2 = A[0]
            min_1 = A[0]
            min_2 = A[0]
            for i in range(len(A)):
                if A[i] > max_1:
                    max_1 = A[i]
                    ind_max = i
                if A[i] < min_1:
                    min_1 = A[i]
                    ind_min = i
            for i in range(len(A)):
                if A[i] > max_2 and i != ind_max:
                    max_2 = A[i]            
                if A[i] < min_2 and i != ind_min:
                    min_2 = A[i]
            if max_1 * max_2 > min_1 * min_2:
                return max_1, max_2
            else:   
                return min_1, min_2
    elif len(A) == 2:
        return A[0], A[1]
    else:
        return A[0]

        
A = list(map(int, input().split()))
print(' '.join(map(str, Digits(A))))