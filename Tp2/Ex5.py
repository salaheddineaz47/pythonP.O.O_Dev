import math


class Point:
    def __init__(self, x=0, y=0):
        self.__abscisse = x
        self.__ordonné = y

    def Afficher(self):
        print(f"POINT({self.__abscisse},{self.__ordonné})")

    def get_abscisse(self):
        return self.__abscisse

    def get_ordonnee(self):
        return self.__ordonné

    def set_abscisse(self, x):
        if isinstance(x, float):
            self.__abscisse = x

    def set_ordonnee(self, y):
        if isinstance(y, float):
            self.__ordonné = y


p1 = Point(5, 5)
print(p1.get_abscisse())
p2 = Point(0, 1)


class Cercle:

    def __init__(self, r, pt):
        self.rayon = r
        self.centre = pt

    def getPerimetre(self):
        return 2 * math.pi * self.rayon

    def getSurface(self):
        return math.pi*self.rayon**2

    def Appartient(self, pt):
        if (pt.get_abscisse() - self.centre.get_abscisse())**2 - (pt.get_ordonnee() - self.centre.get_ordonnee())**2 == self.rayon**2:
            return f"le Point ({pt.get_abscisse()},{pt.get_ordonnee()}) : APPARTIENT AU CERCLE "
        else:
            return f"le Point ({pt.get_abscisse()},{pt.get_ordonnee()}) : N'APPARTIENT PAS AU CERCLE "


c1 = Cercle(5, p1)
print(c1.getPerimetre())
print(c1.getSurface())
print(c1.Appartient(p2))

# c1.Appartient(2, 2)
# Point2 = Point(3, 8)

# print(Point1.Norme())
# print(Point2.Norme())

# p1.Afficher()
