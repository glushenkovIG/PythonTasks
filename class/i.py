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
    
    def __lt__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 / b1 < a2 / b2
        elif type(other) == float:
            b, a = self.b, self.a
            return a / b < float(other)
        elif type(other) == int:
            b, a = self.b, self.a
            return a / b < int(other)            
            
    def __le__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 / b1 <= a2 / b2
        elif type(other) == float:
            b, a = self.b, self.a
            return a / b <= float(other)
        elif type(other) == int:
            b, a = self.b, self.a
            return a / b <= int(other)        
                      
    def __eq__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 / b1 == a2 / b2
        elif type(other) == float:
            b, a = self.b, self.a
            return a / b == float(other)
        elif type(other) == int:
            b, a = self.b, self.a
            return a / b == int(other)        
    
    def __ne__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 / b1 != a2 / b2
        elif type(other) == float:
            b, a = self.b, self.a
            return a / b != float(other)
        elif type(other) == int:
            b, a = self.b, self.a
            return a / b != int(other)        
        
    def __gt__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 / b1 > a2 / b2
        elif type(other) == float:
            b, a = self.b, self.a
            return a / b > float(other)
        elif type(other) == int:
            b, a = self.b, self.a
            return a / b > int(other)        
    
    def __ge__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 / b1 >= a2 / b2
        elif type(other) == float:
            b, a = self.b, self.a
            return a / b >= float(other)
        elif type(other) == int:
            b, a = self.b, self.a
            return a / b >= int(other)        
        
    def __str__(self):
        A = self.reduce()
        if A.b != 1:
            return str(A.a) + '/' + str(A.b)
        return str(A.a)

zero = Fraction()
one = Fraction(1)
half = Fraction('-10/-20')
third = Fraction(1, 3)

print('01: ', zero < one)
print('02: ', zero <= one)
print('03: ', zero <= zero)
print('04: ', zero > one)
print('05: ', zero >= one)
print('06: ', one >= one)
print('07: ', zero == one)
print('08: ', zero == zero)
print('09: ', zero != zero)
print('10: ', zero != one)

print('11: ', 1 < half)
print('12: ', 1 > half)
print('13: ', 0 < half)
print('14: ', 0 > half)
print('15: ', half < 0)
print('16: ', half > 0)
print('17: ', half < 1)
print('18: ', half > 1)
print('19: ', zero == 0)
print('20: ', 1 == one)
print('21: ', zero != 0)
print('22: ', 1 != one)

print('23: ', third < half)
print('24: ', third <= half)
print('25: ', third > half)
print('26: ', third >= half)
print('27: ', third == half)
print('28: ', third != half)

print('29: ', half < third)
print('30: ', half <= third)
print('31: ', half > third)
print('32: ', half >= third)
print('33: ', half == third)
print('34: ', half != third)

print('35: ', 0.4 < half)
print('36: ', 0.4 <= half)
print('37: ', 0.4 > half)
print('38: ', 0.4 >= half)
print('39: ', 0.4 == half)
print('40: ', 0.4 != half)
print('41: ', half < 0.4)
print('42: ', half <= 0.4)
print('43: ', half > 0.4)
print('44: ', half >= 0.4)
print('45: ', half == 0.4)
print('46: ', half != 0.4)

print('47: ', 0.5 < half)
print('48: ', 0.5 <= half)
print('49: ', 0.5 > half)
print('50: ', 0.5 >= half)
print('51: ', 0.5 == half)
print('52: ', 0.5 != half)
print('53: ', half < 0.5)
print('54: ', half <= 0.5)
print('55: ', half > 0.5)
print('56: ', half >= 0.5)
print('57: ', half == 0.5)
print('58: ', half != 0.5)

print('59: ', 0.6 < half)
print('60: ', 0.6 <= half)
print('61: ', 0.6 > half)
print('62: ', 0.6 >= half)
print('63: ', 0.6 == half)
print('64: ', 0.6 != half)
print('65: ', half < 0.6)
print('66: ', half <= 0.6)
print('67: ', half > 0.6)
print('68: ', half >= 0.6)
print('69: ', half == 0.6)
print('70: ', half != 0.6)

print('71: ', 0.333333 < third)
print('72: ', 0.333333 <= third)
print('73: ', 0.333333 > third)
print('74: ', 0.333333 >= third)
print('75: ', 0.333333 == third)
print('76: ', 0.333333 != third)
print('77: ', third < 0.333333)
print('78: ', third <= 0.333333)
print('79: ', third > 0.333333)
print('80: ', third >= 0.333333)
print('81: ', third == 0.333333)
print('82: ', third != 0.333333)

print('83: ', 0.333334 < third)
print('84: ', 0.333334 <= third)
print('85: ', 0.333334 > third)
print('86: ', 0.333334 >= third)
print('87: ', 0.333334 == third)
print('88: ', 0.333334 != third)
print('89: ', third < 0.333334)
print('90: ', third <= 0.333334)
print('91: ', third > 0.333334)
print('92: ', third >= 0.333334)
print('93: ', third == 0.333334)
print('94: ', third != 0.333334)

print('95: ', 1 / 3 < third)
print('96: ', 1 / 3 <= third)
print('97: ', 1 / 3 > third)
print('98: ', 1 / 3 >= third)
print('99: ', 1 / 3 == third)
print('100: ', 1 / 3 != third)
print('101: ', third < 1 / 3)
print('102: ', third <= 1 / 3)
print('103: ', third > 1 / 3)
print('104: ', third >= 1 / 3)
print('105: ', third == 1 / 3)
print('106: ', third != 1 / 3)

A = Fraction(1, 2)
B1 = Fraction(10 ** 20 + 1, 2 * 10 ** 20)
B2 = Fraction(10 ** 20 - 1, 2 * 10 ** 20)
print('107: ', A == B1)
print('108: ', A != B1)
print('109: ', A <= B1)
print('110: ', A >= B1)
print('111: ', A < B1)
print('112: ', A > B1)
print('113: ', A == B2)
print('114: ', A != B2)
print('115: ', A <= B2)
print('116: ', A >= B2)
print('117: ', A < B2)
print('118: ', A > B2)

C1 = Fraction(10 ** 30 - 1, 10 ** 30)
C2 = Fraction(10 ** 30 + 1, 10 ** 30)

print('119: ', C1 == 1)
print('120: ', C1 != 1)
print('121: ', C1 < 1)
print('122: ', C1 > 1)
print('123: ', C1 <= 1)
print('124: ', C1 >= 1)

print('125: ', 1 == C1)
print('126: ', 1 != C1)
print('127: ', 1 < C1)
print('128: ', 1 > C1)
print('129: ', 1 <= C1)
print('130: ', 1 >= C1)

print('131: ', C2 == 1)
print('132: ', C2 != 1)
print('133: ', C2 < 1)
print('134: ', C2 > 1)
print('135: ', C2 <= 1)
print('136: ', C2 >= 1)

print('137: ', 1 == C2)
print('138: ', 1 != C2)
print('139: ', 1 < C2)
print('140: ', 1 > C2)
print('141: ', 1 <= C2)
print('142: ', 1 >= C2)
import sys
exec(sys.stdin.read())