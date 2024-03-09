class Robot:
    '''This class is Robot!'''
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def setEnergy(self, energy):
        self.energy = energy
    def __del__(self):
        print("Robot is destroyed")

    def __str__(self):
        my_str = f'My name is {self.name} and year is {self.year}'
        return my_str

    def __add__(self, other):
        year = self.year + other.year
        return year

    def __eq__(self, other):
        return self.year == other.year

r1 = Robot("Tony", 2000)
r2 = Robot("Gally", 1000)
print(r1.__doc__)
print(f'Robot name: {r1.name}')
r1.setEnergy(500)
print(r1.energy) # same
print(getattr(r1, 'energy')) # same
print(getattr(r1, 'brand', 'N/A'))
print(r1.__dict__)

print(r1)
print(r1 + r2)
# print(r1 < r2) # Error
print(r1 == r2) # Success



