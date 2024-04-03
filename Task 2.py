class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real_part, imaginary_part)
    
    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(real_part, imaginary_part)
    
    def __repr__(self):
        return f"{self.real} + {self.imaginary}i"

complex1 = Complex(3, 4)
complex2 = Complex(2, 1)

print(complex1 + complex2)
print(complex1 - complex2)
print(complex1 * complex2)
print(complex1 / complex2)
