def Shooting(n, POINTS):
    find_max = 0
    max_point = max(POINTS)
    dad_points = 0
    for i in range(n - 1):
        if POINTS[i] == max_point and find_max == 0:
            find_max = 1
        elif find_max == 1 and POINTS[i] % 10 == 5 and POINTS[i] >= dad_points and POINTS[i + 1] < POINTS[i]:
            dad_points = POINTS[i]
    if dad_points != 0:
        index = 0
        POINTS.sort(reverse = True)
        while POINTS[index] != dad_points and index < n:
            index += 1
        return index + 1
    return 0
    

n = int(input())
POINTS = list(map(int, input().split()))
print(Shooting(n, POINTS))