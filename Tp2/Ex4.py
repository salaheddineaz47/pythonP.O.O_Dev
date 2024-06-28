class Produit:
    __total_produits_vendus = 0

    def __init__(self, name="Unknown", price=0, qt=0):
        self.__Nom = name
        self.prix = price
        self.quantity = qt

    def get_Nom(self):
        return self.__Nom

    def set_Nom(self, a):
        self.__Nom = a
# /////////////////////////////////////

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, b):
        if b > 0:
            self.__prix = b
        else:
            print("LE prix est invalide")
# /////////////////////////////////////////

    @property
    def quantity(self):
        return self.__quantite_stock

    @quantity.setter
    def quantity(self, q):
        if q > 0:
            self.__quantite_stock = q
        else:
            print("la quantité est invalide")
# ///////////////////////////

    def vendre_produit(self, qv):
        if self.__quantite_stock >= qv:
            self.__quantite_stock -= qv
            Produit.__total_produits_vendus += qv
        else:
            print("la quantité est indisponible dans le stock")

    @staticmethod
    def afficher_total_vendus():
        return Produit.__total_produits_vendus


P1 = Produit('ahmed', 10, 5)
P2 = Produit('Mohammed', 20, 10)

print(P1.prix)
print(P1.get_Nom())
P1.prix = 15
print(P1.prix)
print(P1.quantity)
P1.quantity = 30
print(P1.quantity)

P1.vendre_produit(10)
print(P1.afficher_total_vendus())
print(P1.quantity)
