class CompteBancaire:
    __taux_interet = None

    def __init__(self, t="Unknown", s=0):
        self.__titulaire = t
        self.Solde = s

    def afficher_infos(self):
        print(f"Le nom : {self.__titulaire}, le solde : {self.__solde}")

    def calculer_interets(self):
        interet = self.__solde * CompteBancaire.__taux_interet
        self.__solde -= interet

    @staticmethod
    def definir_taux_interet(a):
        if isinstance(a, float) and a >= 0 and a <= 1:
            CompteBancaire.__taux_interet = a
        else:
            print("le taux d'interet est invalide")

    def get_titulaire(self):
        return self.__titulaire

    def set_titulaire(self, t):
        self.__titulaire = t

    @property
    def Solde(self):
        return self.__solde

    @Solde.setter
    def Solde(self, s):
        if s > 0:
            self.__solde = s
        else:
            print("Le solde est invalide")


compte1 = CompteBancaire("SALAH", 1000)
compte2 = CompteBancaire("Ahmed", 200)

compte1.afficher_infos()
print(compte1.get_titulaire())
compte1.set_titulaire('MOHAMMED')
print(compte1.get_titulaire())

# CompteBancaire.definir_taux_interet(0.7)
# compte1.calculer_interets()

CompteBancaire.definir_taux_interet(0.2)
compte1.calculer_interets()
compte1.afficher_infos()
