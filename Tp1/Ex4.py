class Rectangle:
    def __init__(self, long="Unknown", larg="unknown"):
        self.Longeur = long
        self.Largeur = larg

    def Perimetre(self):
        return 2*(self.Largeur + self.Longeur)

    def Aire(self):
        return self.Largeur*self.Longeur

    def EstCarre(self):
        if (self.Largeur == self.Longeur):
            return "Il s'agit d'un carré"
        else:
            return "Il ne s'agit pas d'un carré"

    def AfficherRectangle(self):
        print(
            f"Longeur : {self.Longeur} - Largeur : {self.Largeur} - Aire : {self.Aire()} - {self.EstCarre()}")


Rec1 = Rectangle(4, 4)
Rec2 = Rectangle(4, 6)
Rec1.AfficherRectangle()
Rec2.AfficherRectangle()
