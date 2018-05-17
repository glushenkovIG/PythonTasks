import copy


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
        if type(other) == Poly:
            return NotImplemented
        elif type(other) == float:
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
        if type(other) == Poly:
            return NotImplemented
        elif type(other) == float:
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
            if factor != 0 and factor != 0.0:
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
                            if (i == len(self.x) - 1 or A == '') and frac < 0:
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
                        elif pow != 1:
                            A += chr(8304 + pow)
                        elif pow == 1 and i != 1:
                            A += chr(185)

        if A != '':
            return A
        return '0'

    def __add__(self, other):
        poly = self
        if type(other) in [int, float, Fraction]:
            poly.x[0] += other
        elif type(other) == Poly:
            min_poly = Poly()
            if len(poly.x) < len(min_poly.x):
                poly, min_poly = min_poly, poly
            for i in range(len(min_poly.x) - 1):
                poly.x[i] += min_poly.x[i]
        return poly

    def __radd__(self, other):
        print(self, other)
        poly = self
        if type(other) in [int, float, Fraction]:
            poly.x[0] += other
        elif type(other) == Poly:
            min_poly = Poly()
            if len(poly.x) < len(min_poly.x):
                poly, min_poly = min_poly, poly
            for i in range(len(min_poly.x) - 1):
                poly.x[i] += min_poly.x[i]
        return poly

    def __iadd__(self, other):
        if type(other) in [int, float, Fraction]:
            self.x[0] += other
        elif type(other) == Poly:
            if len(self.x) < len(other.x):
                self, other = other, self
            for i in range(len(other.x) - 1):
                self.x[i] += other.x[i]
        return self


import sys
exec(sys.stdin.read())

import random

random.seed(837283918)
__count = 0

def TEST(title = ''):
    global __count
    __count += 1
    print()
    print('=====================================')
    print('Подтест ', __count, ':', title)

def randInt():
    return random.randint(-1000, 1000)

def randFloat():
    return random.random() * 2000 - 1000

def randFraction():
    a = random.randint(-1000, 1000)
    b = random.randint(-1000, 1000)
    while b == 0:
        b = random.randint(-1000, 1000)
    return Fraction(a, b)

def randZero():
    return random.choice([0, 0.0, Fraction(0)])

def Zero():
    return 0

def randCoeff(genFunc = [randInt, randFloat, randFraction, randZero]):
    return random.choice(genFunc)()

def randIntPoly(n=100):
    L = [randInt() for j in range(random.randint(1, n))]
    while L[-1] == 0:
        L[-1] = randInt()
    return Poly(L)

def randFractionPoly(n=100):
    L = [randFraction() for j in range(random.randint(1, n))]
    while L[-1] == 0:
        L[-1] = randFraction()
    return Poly(L)

def randFloatPoly(n=100):
    L = [randFloat() for j in range(random.randint(1, n))]
    while L[-1] == 0:
        L[-1] = randFloat()
    return Poly(L)

def randPoly(n=100):
    L = [randCoeff() for j in range(random.randint(1, n))]
    while L[-1] == 0:
        L[-1] = randCoeff()
    return Poly(L)

print('Тестируются сложение многочленов')
TEST('Метод __add__ для Poly + Poly')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = Poly([1, 5, 7, 1, 2])
_C = _A + _B
print(_C)
_A = Poly([-2, 3, -1, -5, 1, -2])
_B = Poly([1, -5, -7, 1, -2, 3, -3, -1, 2])
_C = _A + _B
print(_C)
_A = Poly([1, 2, 3])
_B = Poly([1, 2, -3])
_C = _A + _B
print(_C)

TEST('Метод __add__ для Poly + int')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = -7
_C = _A + _B
print(_C)
_A = Poly([2, 0, 1])
_B = -2
_C = _A + _B
print(_C)
_A = Poly([Fraction(12, 7), 0, 1])
_B = 1
_C = _A + _B
print(_C)
_A = Poly([1.5, 0, 1])
_B = 1
_C = _A + _B
print(_C)

TEST('Метод __add__ для Poly + Fraction')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = Fraction(19, 4)
_C = _A + _B
print(_C)
_A = Poly([2, 0, 1])
_B = Fraction(-6, 3)
_C = _A + _B
print(_C)
_A = Poly([Fraction(12, 7), 0, 1])
_B = Fraction(-18, 5)
_C = _A + _B
print(_C)
_A = Poly([1.5, 0, 1])
_B = Fraction(14, 9)
_C = _A + _B
print(_C)

TEST('Метод __add__ для Poly + float')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = 12.35
_C = _A + _B
print(_C)
_A = Poly([2, 0, 1])
_B = -2.0
_C = _A + _B
print(_C)
_A = Poly([Fraction(12, 7), 0, 1])
_B = 13.24
_C = _A + _B
print(_C)
_A = Poly([1.5, 0, 1])
_B = 17.81
_C = _A + _B
print(_C)

TEST('Метод __iadd__ для Poly + Poly')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = Poly([1, 5, 7, 1, 2])
_A += _B
print(_A)
_A = Poly([-2, 3, -1, -5, 1, -2])
_B = Poly([1, -5, -7, 1, -2, 3, -3, -1, 2])
_A += _B
print(_A)
_A = Poly([1, 2, 3])
_B = Poly([1, 2, -3])
_A += _B
print(_A)

TEST('Метод __iadd__ для Poly + int')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = -7
_A += _B
print(_A)
_A = Poly([2, 0, 1])
_B = -2
_A += _B
print(_A)
_A = Poly([Fraction(12, 7), 0, 1])
_B = 1
_A += _B
print(_A)
_A = Poly([1.5, 0, 1])
_B = 1
_A += _B
print(_A)

TEST('Метод __iadd__ для Poly + Fraction')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = Fraction(19, 4)
_A += _B
print(_A)
_A = Poly([2, 0, 1])
_B = Fraction(-6, 3)
_A += _B
print(_A)
_A = Poly([Fraction(12, 7), 0, 1])
_B = Fraction(-18, 5)
_A += _B
print(_A)
_A = Poly([1.5, 0, 1])
_B = Fraction(14, 9)
_A += _B
print(_A)

TEST('Метод __iadd__ для Poly + float')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = 12.35
_A += _B
print(_A)
_A = Poly([2, 0, 1])
_B = -2.0
_A += _B
print(_A)
_A = Poly([Fraction(12, 7), 0, 1])
_B = 13.24
_A += _B
print(_A)
_A = Poly([1.5, 0, 1])
_B = 17.81
_A += _B
print(_A)

TEST('Метод __radd__ для Poly + int')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = -7
_C = _B + _A
print(_C)
_A = Poly([2, 0, 1])
_B = -2
_C = _B + _A
print(_C)
_A = Poly([Fraction(12, 7), 0, 1])
_B = 1
_C = _B + _A
print(_C)
_A = Poly([1.5, 0, 1])
_B = 1
_C = _B + _A
print(_C)

TEST('Метод __radd__ для Poly + Fraction')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = Fraction(19, 4)
_C = _B + _A
print(_C)
_A = Poly([2, 0, 1])
_B = Fraction(-6, 3)
_C = _B + _A
print(_C)
_A = Poly([Fraction(12, 7), 0, 1])
_B = Fraction(-18, 5)
_C = _B + _A
print(_C)
_A = Poly([1.5, 0, 1])
_B = Fraction(14, 9)
_C = _B + _A
print(_C)

TEST('Метод __radd__ для Poly + float')
_A = Poly([2, 3, 1, 3, 4, 5, 1, 2])
_B = 12.35
_C = _B + _A
print(_C)
_A = Poly([2, 0, 1])
_B = -2.0
_C = _B + _A
print(_C)
_A = Poly([Fraction(12, 7), 0, 1])
_B = 13.24
_C = _B + _A
print(_C)
_A = Poly([1.5, 0, 1])
_B = 17.81
_C = _B + _A
print(_C)

TEST('Специальные тесты на корректность реализации __iadd__')
_A = Poly([1, 1, 1])
_B = Poly([1, 1])
_D = _A
_A += _B
print(_D)
_A += _B
print(_D)
_A += _B
print(_D)
_A += 1
print(_D)
_A += Fraction(1, 2)
print(_D)
_A += 1.2
print(_D)

for i in range(100):
    TEST('Большой случайный тест')
    if i % 4 == 0:
        _A = randPoly()
        _B = randPoly()
        _x = randCoeff()
    elif i % 4 == 1:
        _A = randIntPoly()
        _B = randIntPoly()
        _x = randInt()
    elif i % 4 == 2:
        _A = randFractionPoly()
        _B = randFractionPoly()
        _x = randFraction()
    elif i % 4 == 3:
        _A = randFloatPoly()
        _B = randFloatPoly()
        _x = randFloat()
    _C = _A + _B
    _D = Poly(_A)
    _D += _B
    _E = _A + _x
    _F = Poly(_A)
    _F += _x
    _G = _x + _A
    print("Source data:")
    print("A = ", _A)
    print("B = ", _B)
    print("x = ", _x)
    print("Result:")
    print("C = ", _C)
    print("D = ", _D)
    print("E = ", _E)
    print("F = ", _F)
    print("G = ", _G)
    print(Poly('1 2 2 2 2 2 2 -1.1  ') * Poly('3 3 3 5 5 6 7 8 8 8 7 6 6 '))
'''import sys
exec(sys.stdin.read())'''