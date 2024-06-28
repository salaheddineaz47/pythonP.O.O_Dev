# class Client:
#     def __init__(self, n="EE2578", m="Unknown", c="Unknown", t=0):
#         self.__Cin = n
#         self.__Nom = m
#         self.__Prenom = c
#         self.__Tel = t

#     def afficher(self):
#         print(f"{self.Nom} {self.__Prenom} / CIN : {self.__Cin} / N°TEL : {self.__Tel}")

#     @property
#     def CIN(self):
#         return self.__Cin

#     @CIN.setter
#     def CIN(self, b):
#         self.__Cin = b

#     @property
#     def Nom(self):
#         return self.__Nom

#     @Nom.setter
#     def Nom(self, b):
#         self.__Nom = b

#     @property
#     def Prenom(self):
#         return self.__Prenom

#     @Prenom.setter
#     def Prenom(self, b):
#         self.__Prenom = b

#     @property
#     def Telephone(self):
#         return self.__Tel

#     @Telephone.setter
#     def Tel(self, b):
#         if isinstance(b, int):
#             self.__Tel = b


class CompteBancaire:
    __count = 0

    def __init__(self, s=0):
        self.__solde = s
        CompteBancaire.__count += 1
        self.__code = CompteBancaire.__count

    @property
    def solde(self):
        return self.__solde

    @property
    def code(self):
        return self.__code

    def Crediter(self, somme):
        if somme > 0:
            self.__solde += somme

    def Debiter(self, somme):
        self.__solde -= somme

    def __str__(self):
        # le proprietaire : {self.__prop.Nom, self.__prop.Prenom}
        return f" , le numero de compte {self.__code}:  , le solde : {self.__solde}"


class CompteEpargne(CompteBancaire):
    __taux_interet = None

    def __init__(self, s=0):
        super().__init__(s)

    def calculer_interets(self):
        interet = self.solde * CompteEpargne.__taux_interet
        self.Crediter(interet)

    @staticmethod
    def get_taux_interet():
        return CompteEpargne.__taux_interet

    @staticmethod
    def definir_taux_interet(a):
        if isinstance(a, float) and a >= 0 and a <= 1:
            CompteEpargne.__taux_interet = a
        else:
            print("le taux d'interet est invalide")

    def __str__(self):
        return super().__str__() + f"Le taux d'interet est {CompteEpargne.__taux_interet}"


class ComptePayant(CompteBancaire):
    def __init__(self, s=0):
        super().__init__(s)

    def Debiter(self, somme):
        super().Debiter(somme)
        super().Debiter(1)
        # super().Debiter(somme + 1)

    def Crediter(self, somme):
        super().Crediter(somme)
        super().Debiter(1)
    #     super().Crediter(somme - 1)

    def __str__(self):
        return super().__str__()


# cb = CompteBancaire(4000)
# print(cb)
# cb.Crediter(500)
# print(cb)
# cb.Debiter(500)
# print(cb)


# ce = CompteEpargne(1000)
# print(ce)
# CompteEpargne.definir_taux_interet(0.2)
# print(CompteEpargne.get_taux_interet())
# ce.calculer_interets()
# print(ce.solde)
# print(ce)

cp = ComptePayant(500)
print(cp)
# print(cp.solde)
cp.Crediter(10)
print(cp)
cp.Debiter(10)
print(cp)
# print(cp.solde)
