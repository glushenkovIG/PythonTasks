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
        self.a = int(self.a // a)
        self.b = int(self.b // a)
    
    def __add__(self, other):
        if type(other) == float:
            return self.a / self.b + other
        elif type(self) == float:
            return other.a / other.b + self        
        else:
            self, other = Fraction(self), Fraction(other)
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            A = Fraction()
            A.a, A.b = a1 * b2 + a2 * b1, b1 * b2
            return A
         
    def __radd__(self, other):
        if type(other) == float:
            return self.a / self.b + other
        elif type(self) == float:
            return other.a / other.b + self        
        else:
            self, other = Fraction(self), Fraction(other)
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            A = Fraction()
            A.a, A.b = a1 * b2 + a2 * b1, b1 * b2
            return A
    
    def _iadd__(self, other):
        if type(other) == float:
            self = self.a / self.b + other
            return self
        elif type(self) == float:
            self = other.a / other.b + self
            return self
        else:
            self, other = Fraction(self), Fraction(other)
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            self.a, self.b = a1 * b2 + a2 * b1, b1 * b2
            return A
        
    def __sub__(self, other):
        if type(other) == float:
            return self.a / self.b - other
        elif type(self) == float:
            return -other.a / other.b + self        
        else:
            self, other = Fraction(self), Fraction(other)
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            A = Fraction()
            A.a, A.b = a1 * b2 - a2 * b1, b1 * b2
            return A
         
    def __rsub__(self, other):
        if type(other) == float:
            return -self.a / self.b + other
        elif type(self) == float:
            return -other.a / other.b + self    
        else:
            self, other = Fraction(self), Fraction(other)
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            A = Fraction()
            A.a, A.b = -a1 * b2 + a2 * b1, b1 * b2
            return A
    
    def _isub__(self, other):
        if type(other) == float:
            self = self.a / self.b - other
            return self
        elif type(self) == float:
            self = -other.a / other.b + self
            return self
        else:
            self, other = Fraction(self), Fraction(other)
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            self.a, self.b = a1 * b2 - a2 * b1, b1 * b2
            return A
    
    def __str__(self):
        self.reduce()
        if self.b != 1:
            return str(str(self.a) + '/' + str(self.b))
        return str(self.a)


import sys
exec(sys.stdin.read())