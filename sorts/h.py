def archive(a, k):
    amount = 0
    A = []
    i = 0
    while i != k:
        i += 1
        A.append(int(input()))
    A.sort()
    elem = A[0]
    while amount != k and a >= A[0]:    
        amount += 1
        elem = A[0]
        a -= A[0] 
        A.pop(0)
    return amount
    
 
a, k = list(map(int, input().split()))
print(archive(a, k))
