def SelektionSort(A):
    NEW = []
    for i in range(len(A)):
        NEW.append(A.pop(A.index(max(A))))
    return NEW
        
        
A = list(map(int, input().split()))
print(' '.join(map(str, SelektionSort(A))))