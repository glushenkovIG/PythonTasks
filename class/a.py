class Point:
    def __init__(self, x, y = ''):
        if y == '':
            self.x, self.y = list(map(int, x.split()))
        else:
            self.x = int(x)
            self.y = int(y)

    def lenVect(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5  
    
    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    
    def __mul__(self, other):
        return self.x * other.x, self.y * other.y
    
    def __lt__(self, other):
        return self.dist() < other.dist()
    
    def __str__(self):
            return str(self.x) + ' ' + str(self.y)
        
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    
n = int(input())
max_dot = Point(0, 0)
for i in range(n):
    x, y = list(map(str, input().split()))
    A = Point(x, y)
    if max_dot < A:
        max_dot = A
print(max_dot)

