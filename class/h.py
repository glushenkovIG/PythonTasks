class Fraction:
    def __init__(self, x = '', y = 0):
        if type(x) == Fraction:
            self.a = x.a
            self.b = x.b
        elif x == '' and y == 0:
            self.a = 0
            self.b = 1
        elif y == 0:
            if '/' in str(x):
                self.a, self.b = list(map(int, x.split('/')))
            elif ' ' in str(x):
                self.a, self.b = list(map(int, x.split()))
            else:
                self.a = int(x)
                self.b = 1              
        else:
            self.a = x
            self.b = y
            
    def reduce(self):
        a, b = self.a, self.b
        while b:
            a, b = b, a % b
        self.a = int(self.a / a)
        self.b = int(self.b / a)
        return self
    
    def __str__(self):
        A = self.reduce()
        if A.b != 1:
            return str(A.a) + '/' + str(A.b)
        return str(A.a)


import sys
exec(sys.stdin.read())