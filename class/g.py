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
        a = self.a
        b = self.b
        while b:
            a, b = b, a % b
        self.a = self.a // a
        self.b = self.b // a
    
    def __str__(self):
        self.reduce()
        if self.b != 1:
            return str(self.a) + '/' + str(self.b)
        return str(self.a)

input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = a = input.readline()
while a:
    print(Fraction(a))
    a = input.readline()