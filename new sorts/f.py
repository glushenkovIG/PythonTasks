n = int(input())
A = list(map(int, input().split()))
second = 0
find_or_not = False
main = -1
while not find_or_not:
    main += 1
    second = main
    while second + 1 < n:
        if A[main] == A[second + 1]:
            find_or_not = True
            break
        second += 1
print(A[main])