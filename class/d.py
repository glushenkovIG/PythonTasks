class Point:
    def __init__(self, x, y = ''):
        if y == '':
            self.x, self.y = list(map(int, x.split()))
        else:
            self.x = x
            self.y = y
            
    def __add__(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)
    
    def __lt__(self, other):
            return self.dist() < other.dist()    
        
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)


n = int(input())
Points = []
for i in range(n):
    A = Point(input())
    Points.append(A)
Points = sorted(Points)
print('\n'.join(list(map(str, Points))))
    
    

