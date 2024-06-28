class Produit:
    def __init__(self, name="Unknown", price=0):
        self.__Nom = name
        self.prix = price

    def get_Nom(self):
        return self.__Nom

    def set_Nom(self, name):
        self.__Nom = name

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, p):
        if p > 0:
            self.__prix = p
        else:
            print("LE prix est invalide")

    def __str__(self):
        return f"le nom : {self.__Nom}, le prix : {self.__prix}, "

    def calculer_prix_final(self):
        return self.__prix


class ProduitElectronique(Produit):
    def __init__(self, name="Unknown", price=0, m="", gar=None):
        super().__init__(name, price)
        self.__marque = m
        self.__garantie = gar

    def get_marque(self):
        return self.__marque

    def set_marque(self, m):
        self.__marque = m

    def get_garantie(self):
        return self.__garantie

    def set_garantie(self, g):
        if isinstance(g, float) and g > 0:
            self.__garantie = g

    def prolonger_garantie(self, duree):
        if isinstance(duree, float) and duree > 0:
            self.__garantie += duree

    def __str__(self):
        return super().__str__() + f"la marque est {self.__marque}, la duree de guarantie est {self.__garantie}"


class ProduitEnPromotion(Produit):
    def __init__(self, name="Unknown", price=0, prc=0):
        super().__init__(name, price)
        self.set_pourcentage_reduction(prc)

    def get_pourcentage_reduction(self):
        return self.__pourcentage_reduction

    def set_pourcentage_reduction(self, m):
        if m >= 0 and m <= 100:
            self.__pourcentage_reduction = m

    def calculer_reduction(self):
        return self.prix * self.__pourcentage_reduction / 100

    def calculer_prix_final(self):
        return super().calculer_prix_final() - self.calculer_reduction()

    def __str__(self):
        return super().__str__() + f"le pourcentage de réduction est {self.__pourcentage_reduction}"


P1 = Produit('ahmed', 10)
P2 = ProduitElectronique('Mohammed', 20, 'Ferrari', 6)
P3 = ProduitEnPromotion('Moha', 300,  10)
print(P3.calculer_reduction())
print(P3.calculer_prix_final())
print(P2)
print(P3)
