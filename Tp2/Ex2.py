class Vehicule:

    def __init__(self, m="Ferrari", mod=2020, a=2023):
        self.__marque = m
        self.__modele = mod
        self.annee = a

    def afficher_details(self):
        print(
            f"La marque : {self.__marque} , le modèle : {self.__modele} , l'année d fabrication : {self.__annee} ")

    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, a):
        if a > 0:
            self.__annee = a
        else:
            print("La date doit etre positif")

    @property
    def marque(self):
        return self.__marque

    @marque.setter
    def marque(self, m):
        self.__marque = m

    @property
    def modele(self):
        return self.__modele

    @modele.setter
    def modele(self, s):
        self.__modele = s


V1 = Vehicule("Renault", 1999, 1992)
V1.afficher_details()

# print(V1.annee)
# print(V1.marque)
# print(V1.modele)

# V1.marque = "LAMBO"
# V1.modele = 1987
# V1.annee = 1990

# V1.afficher_details()
