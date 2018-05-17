class Point:
    def __init__(self, x, y = ''):
        if type(x) == str:
            self.x, self.y = list(map(int, x.split()))
        else:
            self.x = x
            self.y = y
            
    def __sub__(self, other):
        A = Point(self.x - other.x, self.y - other.y)
        return A
       
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    
    def __mul__(self, other):
        return self.x * other.x, self.y * other.y
    
    def __lt__(self, other):
        return self.dist() < other.dist()
    
    def __str__(self):
            return str(self.x) + ' ' + str(self.y)
        
        
def Perimeter(A, B, C):
    a = (A - B).dist()
    b = (C - B).dist()
    c = (A - C).dist()
    return ((a + b + c) * (b + c - a) * (a + c - b) * (a + b - c)) ** 0.5 / 4
    

n = int(input())
Points = dict()
for i in range(n):
    A = Point(input())
    Points[i] = A
Area = 0
maxArea = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            Area = Perimeter(Points[i], Points[j], Points[k])
            if maxArea < Area:
                maxArea = Area
print(maxArea)