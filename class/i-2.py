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
        return self
    
    def __lt__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 * b2 < a2 * b1
        elif type(other) == int or type(other) == float:
            self = self.reduce()
            b, a = self.b, self.a
            return a < other * b
            
    def __le__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 * b2 <= a2 * b1
        elif type(other) == int or type(other) == float:
            self = self.reduce()
            b, a = self.b, self.a
            return a <= other * b
            
    def __eq__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = int(self.a), int(other.a)
            return a1 * b2 == a2 * b1
        elif type(other) == int or type(other) == float:
            self = self.reduce()
            b, a = self.b, self.a
            return a == other * b        
    
    def __ne__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 * b2 != a2 * b1
        elif type(other) == int or type(other) == float:
            self = self.reduce()
            b, a = self.b, self.a
            return a != other * b           
        
    def __gt__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 * b2 > a2 * b1
        elif type(other) == int or type(other) == float:
            self = self.reduce()
            b, a = self.b, self.a
            return a > other * b            
    
    def __ge__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 * b2 >= a2 * b1
        elif type(other) == int or type(other) == float:
            self = self.reduce()
            b, a = self.b, self.a
            return a >= other * b
        
    def __str__(self):
        A = self.reduce()
        if A.b != 1:
            return str(A.a) + '/' + str(A.b)
        return str(A.a)
    

import random

random.seed(12352583)

for _i in range(2000):
    _a = random.randint(-10 ** 6, 10 ** 6)
    _b = random.randint(-10 ** 6, 10 ** 6)
    while _b == 0:
        _b = random.randint(-10 ** 6, 10 ** 6)
    _c = random.randint(-10 ** 6, 10 ** 6)
    _d = random.randint(-10 ** 6, 10 ** 6)
    while _d == 0:
        _d = random.randint(-10 ** 6, 10 ** 6)
    _frac1 = Fraction(_a, _b)
    _frac2 = Fraction(_c, _d)
    print(_a, _b, _c, _d, _frac1, _frac2)
    print(_frac1, _frac2, _frac1 < _frac2, _frac1 <= _frac2, _frac1 > _frac2, _frac1 >= _frac2, _frac1 == _frac2, _frac1 != _frac2, _frac1 == _frac1, _frac1 != _frac1)
    _int1 = _a // _b
    _int2 = _int1 + 1
    print(_int1, _frac1, _int1 < _frac1, _int1 <= _frac1, _int1 > _frac1, _int1 >= _frac1, _int1 == _frac1, _int1 != _frac1)
    print(_frac1, _int1, _frac1 < _int1, _frac1 <= _int1, _frac1 > _int1, _frac1 >= _int1, _frac1 == _int1, _frac1 != _int1)
    print(_int2, _frac1, _int2 < _frac1, _int2 <= _frac1, _int2 > _frac1, _int2 >= _frac1, _int2 == _frac1, _int2 != _frac1)
    print(_frac1, _int2, _frac1 < _int2, _frac1 <= _int2, _frac1 > _int2, _frac1 >= _int2, _frac1 == _int2, _frac1 != _int2)
    _float1 = _c / _d
    _float2 = _float1 - 0.0001
    _float3 = _float1 + 0.0001
    print(_float2, _frac2, _float2 < _frac2, _float2 <= _frac2, _float2 > _frac2, _float2 >= _frac2, _float2 == _frac2, _float2 != _frac2)
    print(_frac2, _float2, _frac2 < _float2, _frac2 <= _float2, _frac2 > _float2, _frac2 >= _float2, _frac2 == _float2, _frac2 != _float2)
    print(_float3, _frac2, _float3 < _frac2, _float3 <= _frac2, _float3 > _frac2, _float3 >= _frac2, _float3 == _frac2, _float3 != _frac2)
    print(_frac2, _float3, _frac2 < _float3, _frac2 <= _float3, _frac2 > _float3, _frac2 >= _float3, _frac2 == _float3, _frac2 != _float3)
