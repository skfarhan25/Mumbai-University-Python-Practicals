from cmath import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def calc_area(self):
        return pi * (self.radius ** 2)

circ = Circle(5)
print(f"Radius of the circle is {circ.get_radius()}")
print(f"Area of the circle is {round(circ.calc_area())}")

