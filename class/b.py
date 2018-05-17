class Point:
    def __init__(self, x, y = ''):
        if type(x) == str:
            self.x, self.y = list(map(int, x.split()))
        else:
            self.x = x
            self.y = y
        
    def __add__(self, other):
        return Point((self.x + other.x), (self.y + other.y))
    
    def __mul__(self, n):
        return self.x * n, self.y * n
    
    def __truediv__(self, n):
        return str(self.x / n) + ' ' + str(self.y / n)
    
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)


n = int(input())
centrWeigh = Point(0, 0)
for i in range(n):
    A = Point(input())
    centrWeigh = A + centrWeigh
print(centrWeigh / n)


