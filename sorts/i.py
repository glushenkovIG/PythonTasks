def Shoe(size):
    amount = 0
    new_size = size
    All_shoe.sort()
    for i in range(len(All_shoe)):
        if All_shoe[i] >= new_size:
            amount += 1
            new_size = All_shoe[i] + 3
    return amount
        
        
size = int(input())
All_shoe = list(map(int, input().split()))
print(Shoe(size))
