def Flaviy(n, k):
        while n != 1:
                return (Flaviy(n - 1, k) + k - 1) % n + 1
        return 1


n, k = list(map(int, input().split()))
print(Flaviy(n, k))