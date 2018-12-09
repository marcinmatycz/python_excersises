import numpy as np


class Complex(object):

    def __init__(self, real, imag = 0.0):
        self.real = real
        self.imag = imag

    def __eq__(self, other):
        return self.real == other.real, self.imag == other.imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        r = float(other.real ** 2 + other.imag ** 2)
        return Complex((self.real * other.real + self.real * other.imag) / r, (self.imag * other.real - self.real * other.imag) / r)

    def __abs__(self):
        return np.sqrt(self.real ** 2 + self.imag ** 2)

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    def print(self):
        if self.imag >= 0:
            print(str(self.real)+"+"+str(self.imag)+"i")
        else:
            print(str(self.real)+str(self.imag)+"i")

    def angle(self):
        return np.arctan2(self.imag, self.real) * 180 / np.pi


z1 = Complex(1, 1)
z1.print()
z2 = Complex(2, 2)
z2.print()

z3 = z1
z3.print()

z3 = z1 + z2
z3.print()

z3 = z1 - z2
z3.print()

z3 = z1*z2
z3.print()

z3 = z1/z2
z3.print()

z3 = abs(z3)
print(z3)

z3 = -z1
z3.print()

print(z3.angle())

