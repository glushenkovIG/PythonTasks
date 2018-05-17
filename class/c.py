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
        return self.x / n, self.y / n
    
    def __sub__(self, other):
        A = Point(self.x - other.x, self.y - other.y)
        return A
    
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)


n = int(input())
d = 0
max_d = 0
Coord = []
for i in range(n):
    A = Point(input())
    Coord.append(A)
for i in range(n):
    for j in range(i + 1, n):
        d = (Coord[i] - Coord[j]).dist()
        if max_d < d:
            max_d = d
print(max_d)