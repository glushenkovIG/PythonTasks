def Keyboard(n, k):
    pressing = [0] * n
    for elem in max_pressing:
        pressing[elem - 1] += 1
    for i in range(n):
        if endurance[i] >= pressing[i]:
            print('NO')
        else:
            print('YES')
n = int(input())
endurance = list(map(int, input().split()))
k = int(input())
max_pressing = list(map(int, input().split()))
Keyboard(n, k)
    