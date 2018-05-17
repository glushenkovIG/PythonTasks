def Olymp(n):
    q = 0
    All_people = []
    while q != n:
        surname, points = list(map(str, input().split()))
        All_people.append((int(points), surname))
        All_people.sort(reverse = True)
        q += 1
    for i in range(n):
        print(All_people[i][1])
    
n = int(input())
Olymp(n)