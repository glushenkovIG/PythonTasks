import copy
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
        self.reduce()

    def __str__(self):
        self.reduce()
        if self.b != 1:
            return str(str(self.a) + '/' + str(self.b))
        return str(self.a)

    def reduce(self):
        a, b = self.a, self.b
        while b:
            a, b = b, a % b
        self.a //= a
        self.b //= a

    def __lt__(self, other):
        if type(other) == Fraction:
            if self.b < 0:
                self.b = -self.b
                self.a = -self.a
            if other.b < 0:
                other.b = -other.b
                other.a = -other.a
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 * b2 < a2 * b1
        elif type(other) == int or type(other) == float:
            self.reduce()
            b, a = self.b, self.a
            return a < other * b

    def __le__(self, other):
        if type(other) == Fraction:
            if self.b < 0:
                self.b = -self.b
                self.a = -self.a
            if other.b < 0:
                other.b = -other.b
                other.a = -other.a
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 * b2 <= a2 * b1
        elif type(other) == int or type(other) == float:
            self.reduce()
            b, a = self.b, self.a
            return a <= other * b

    def __eq__(self, other):
        if type(other) == Fraction:
            if self.b < 0:
                self.b = -self.b
                self.a = -self.a
            if other.b < 0:
                other.b = -other.b
                other.a = -other.a
            b1, b2 = self.b, other.b
            a1, a2 = int(self.a), int(other.a)
            return a1 * b2 == a2 * b1
        elif type(other) == int or type(other) == float:
            self.reduce()
            b, a = self.b, self.a
            return a == other * b

    def __ne__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 * b2 != a2 * b1
        elif type(other) == int or type(other) == float:
            self.reduce()
            b, a = self.b, self.a
            return a != other * b

    def __gt__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 * b2 > a2 * b1
        elif type(other) == int or type(other) == float:
            self.reduce()
            b, a = self.b, self.a
            return a > other * b

    def __ge__(self, other):
        if type(other) == Fraction:
            b1, b2 = self.b, other.b
            a1, a2 = self.a, other.a
            return a1 * b2 >= a2 * b1
        elif type(other) == int or type(other) == float:
            self.reduce()
            b, a = self.b, self.a
            return a >= other * b

    def __int__(self):
        return self.a // self.b

    def __float__(self):
        return self.a / self.b

    def __round__(self, x = 0):
        return round(self.a / self.b, x)

    def __pos__(self):
        return Fraction(+self.a, self.b)

    def __abs__(self):
        return Fraction(abs(self.a), abs(self.b))

    def __neg__(self):
        self = Fraction(self)
        return Fraction(-self.a, self.b)

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

    def __mul__(self, other):
        if type(other) == float:
            return self.a / self.b * other
        other = Fraction(other)
        A = (Fraction(self.a * other.a, self.b * other.b))
        A.reduce()
        return A

    def __rmul__(self, other):
        if type(other) == float:
            return self.a / self.b * other
        self, other = Fraction(self), Fraction(other)
        A = (Fraction(self.a * other.a, self.b * other.b))
        A.reduce()
        return A

    def __imul__(self, other):
        if type(other) == float:
            return self.a / self.b * other
        other = Fraction(other)
        self = (Fraction(self.a * other.a, self.b * other.b))
        self.reduce()
        return self

    def __truediv__(self, other):
        if type(other) == float:
            return self.a / self.b / other
        other = Fraction(other)
        A = (Fraction(self.a * other.b, self.b * other.a))
        A.reduce()
        return A

    def __rtruediv__(self, other):
        if type(other) == float:
            return other / (self.a / self.b)
        self, other = Fraction(self), Fraction(other)
        A = (Fraction(self.b * other.a, self.a * other.b))
        A.reduce()
        return A

    def __itruediv__(self, other):
        if type(other) == float:
            return self.a / self.b / other
        other = Fraction(other)
        self = (Fraction(self.a * other.b, self.b * other.a))
        self.reduce()
        return self


class Poly():
    def __init__(self, x = [0]):
        if type(x) in [int, Fraction, float]:
            self.x = [x]
        elif type(x) == list:
            self.x = copy.deepcopy(x)
        elif type(x) == str:
            b = []
            for elem in x.split():
                b.append(eval(elem))
            self.x = b
        elif x == [0]:
            self.x = [0]
        elif type(x) == Poly:
            self.x = copy.deepcopy(x.x)
        elif type(x) == tuple:
            self.x = list(x)            

    def __str__(self):
        A = ''
        for i in range(len(self.x) - 1, -1, -1):
            factor = self.x[i]
            if factor != 0:
                if factor > 0 and len(A) != 0:
                    A += ' + '
                elif len(A) != 0:
                    A += ' - '
                    factor = -factor
                if factor != 1 or i == 0:
                    if type(factor) == float:
                        factor = round(factor, 3)
                    if type(factor) == Fraction:
                        frac = factor.a / factor.b
                        if frac == int(frac):
                            factor = int(frac)
                        else:
                            if i == len(self.x) - 1 and factor < 0:
                                factor = -factor
                                factor = '-' + '(' + str(factor) + ')'
                                
                            else:
                                factor = '(' + str(factor) + ')'
                    A += str(factor)
                if i != 0:
                    A += 'x'
                    for elem in str(i):
                        pow = int(elem)
                        if pow == 2 or pow == 3:
                            A += chr(176 + pow)
                        elif i != 1:
                            A += chr(8304 + pow)
        if A != '':
            return A
        return '0'
        
        
import sys
exec(sys.stdin.read())