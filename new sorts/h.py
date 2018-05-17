n = int(input())
COORD = []
distance = 0
max_distance = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    COORD.append([x, y])
for elem in COORD:
    for i in range(len(COORD)):
        distance = ((elem[0] - COORD[i][0]) ** 2 + (elem[1] - COORD[i][1]) ** 2) ** (1 / 2)
        if distance > max_distance:
            max_distance = distance
print(max_distance)
            
        
    
