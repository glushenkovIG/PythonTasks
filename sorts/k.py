def Papers(n):
    All_people = []
    for i in range(n):
        surname, points = list(map(str, input().split()))
        All_people.append((int(points), surname))
        All_people.sort()        
    for i in range(n):
        print(' '.join(map(str, All_people[i])))
n = int(input())
Papers(n)