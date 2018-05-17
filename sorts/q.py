def SMS(n):
    COUNT_OPINIONS = [0] * (n + 1)
    for elem in OPINIONS:
        if elem <= n:
            COUNT_OPINIONS[elem] += 1
    i = 0
    winners = []
    max_ = max(COUNT_OPINIONS)
    while i != n + 1:
        if COUNT_OPINIONS[i] == max_:
            winners.append(i)
        i += 1
    winners.sort()
    return winners
        
n = int(input())
OPINIONS = list(map(int, input().split()))
print(' '.join(map(str, SMS(n))))
        