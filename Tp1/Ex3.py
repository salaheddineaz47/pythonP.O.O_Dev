import math


class Point:
    def __init__(self, x=0, y=0):
        self.abscisse = x
        self.ordonné = y

    def Norme(self):
        d = math.sqrt(self.abscisse**2 +
                      self.ordonné**2)
        return d


Point1 = Point(12, 5)
Point2 = Point(3, 8)

print(Point1.Norme())
print(Point2.Norme())
