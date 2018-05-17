n = int(input())
A = list(map(int, input().split()))
way = 0
way_max = 0
for i in range(n):
    way = 0
    if A[i] == 1:
        right_ind = i
        while right_ind < n and A[right_ind] != 2:
            right_ind += 1
        if right_ind != n:    
            way = right_ind - i
        else:
            way = n
        left_ind = i
        while left_ind != -1 and A[left_ind] != 2:
            left_ind -= 1
        if left_ind != -1:    
            if i - left_ind < way:
                way = i - left_ind
    if way > way_max:
        way_max = way
print(way_max)