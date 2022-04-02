import math


class Sphere:

    def __init__(self, rad):
        self.rad = rad

    def volume(self):
        return round(4 / 3 * math.pi * (self.rad ** 3), 2)

    def surface_area(self):
        return round(4 * math.pi * (self.rad ** 2), 2)

MySphere = Sphere(5)
print(f"Volume of my Sphere {MySphere.volume()}")
print(f"Surface Area of my Sphere {MySphere.surface_area()}")

