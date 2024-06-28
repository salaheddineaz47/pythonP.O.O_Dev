class Livre:
    def __init__(self, a="Unknown", t="title unknown", p=10):
        self.__auteur = a
        self.__titre = t
        self.set_prix(p)

    def aficher_details(self):
        print(
            f"l'auteur du Livre titulé {self.__titre} est {self.__auteur}, Le PRIX : {self.__prix} dh .")

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, a):
        self.__auteur = a

    def get_titre(self):
        return self.__titre

    def set_titre(self, t):
        self.__titre = t

    def get_prix(self):
        return self.__prix

    def set_prix(self, p):
        if p > 0:
            self.__prix = p
        else:
            print("Valeur invalide")


Livre1 = Livre("Victor Hugo", "Les misérables", 20)

# Livre1.__titre = "salaj"
# Livre1.__auteur = "mohammed"
print(Livre1.get_auteur())
print(Livre1.get_titre())
print(Livre1.get_prix())

Livre1.set_auteur("Ahmed")
Livre1.set_titre("Antigone")
Livre1.set_prix(100)

Livre1.aficher_details()
