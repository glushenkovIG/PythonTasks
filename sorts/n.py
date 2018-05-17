def Skises(SKI, SIZES):
    amount = 0
    SKI.sort()
    SIZES.sort()
    a = len(SIZES)
    while len(SKI) != 0 and len(SIZES) != 0:
        if SIZES[0] <= SKI[0]:
            amount += 1
            SIZES.pop(0)
            SKI.pop(0)
        else:
            SKI.pop(0)
    return amount
                

SKI = list(map(int, input().split()))
SIZES = list(map(int, input().split()))
print(Skises(SKI, SIZES))

                