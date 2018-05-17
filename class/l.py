def fastPow(a, n):
    res = 1
    while n:
        if n & 1:
            res *= a
        n = n >> 1
        if n == 0:
            break
        a *= a
    return res


class Fraction:
    def __init__(self, x = '', y = 0, IS = True):
        if type(x) == Fraction:
            self.a = x.a
            self.b = x.b
        if type(x) == float:
            b1 = 1
            while int(x) != float(x):
                x *= 10
                b1 *= 10
            self.a, self.b = int(x), b1 * y
        if x == '' and y == 0:
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
        self.Is = IS
        
    def __pow__(self, other):
        if type(other) == float or type(other) == Fraction:
            return (self.a / self.b) ** other
        if type(other) == int:
            if other < 0:
                other = -other
                return Fraction(fastPow(self.b, other), fastPow(self.a, other))
            return Fraction(fastPow(self.a, other), fastPow(self.b, other))
        
    def __rpow__(self, other):
        return other ** (self.a / self.b)
    
    def __ipow__(self, other):
        self = self.reduce()
        if type(other) == float or type(other) == Fraction:
            return (self.a / self.b) ** other
        else:
            if other < 0:
                other = -other
                self = Fraction(fastPow(self.b, other), fastPow(self.a, other))
                return self
            self = Fraction(fastPow(self.a, other), fastPow(self.b, other), False)
            return self
     
    def reduce(self, Is = True):
        Is = self.Is
        if not Is:
            return self
        a, b = self.a, self.b
        while b:
            a, b = b, a % b
        self.a = int(self.a // a)
        self.b = int(self.b // a)
        return self
    
    def __str__(self):
        A = self.reduce()
        if A.b != 1:
            return str(str(A.a) + '/' + str(A.b))
        return str(A.a)


import sys
exec(sys.stdin.read())