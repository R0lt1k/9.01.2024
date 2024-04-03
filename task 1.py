class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __ge__(self, other):
        return self.radius >= other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius
    
    def __add__(self, value):
        return Circle(self.radius + value)
    
    def __sub__(self, value):
        return Circle(abs(self.radius - value))
    
    def __iadd__(self, value):
        self.radius += value
        return self
    
    def __isub__(self, value):
        self.radius -= value
        return self
    
    def __repr__(self):
        return f"Circle with radius {self.radius}"

radius1 = Circle(5)
radius2 = Circle(7)

print(radius1 == radius2)
print(radius1 > radius2)
print(radius1 + 3)
print(radius1 - 2)
radius1 += 2
print(radius1)
