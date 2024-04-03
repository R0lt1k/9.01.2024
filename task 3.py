class Airplane:
    def __init__(self, model, max_passengers, current_passengers=0):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers
    
    def __eq__(self, other):
        return self.model == other.model
    
    def __gt__(self, other):
        return self.max_passengers > other.max_passengers
    
    def __lt__(self, other):
        return self.max_passengers < other.max_passengers
    
    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers
    
    def __le__(self, other):
        return self.max_passengers <= other.max_passengers
    
    def __add__(self, passengers):
        new_passengers = self.current_passengers + passengers
        if new_passengers <= self.max_passengers:
            self.current_passengers = new_passengers
        else:
            print("Exceeding maximum capacity!")
        return self
    
    def __sub__(self, passengers):
        new_passengers = self.current_passengers - passengers
        if new_passengers >= 0:
            self.current_passengers = new_passengers
        else:
            print("Cannot have negative passengers!")
        return self
    
    def __iadd__(self, passengers):
        return self.__add__(passengers)
    
    def __isub__(self, passengers):
        return self.__sub__(passengers)
    
    def __repr__(self):
        return f"{self.model} - Max Passengers: {self.max_passengers}, Current Passengers: {self.current_passengers}"

plane1 = Airplane("Boeing 767", 2001, 800)
plane2 = Airplane("Airbus A320", 180, 120)

print(plane1 == plane2)
print(plane1 > plane2)

plane1 += 111
print(plane1)

plane2 -= 50
print(plane2)
