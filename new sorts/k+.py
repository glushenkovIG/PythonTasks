n, m = list(map(int, input().split()))
ind = 0
A = list(map(int, input().split()))
B = list(map(int, input().split()))
while ind != n and ind != m:
    if A[ind] != B[ind]:
        if A[ind] > B[ind]:
            print('greater')
            break
        elif A[ind] < B[ind]:
            print('less')
            break
    ind += 1
    if ind == n and ind == m:
        print('equal')
    elif ind == n and ind != m:
        print('less')
    elif ind != n and ind == m:
        print('greater')
        