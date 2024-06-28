class Client:
    def __init__(self, n="EE2578", m="Unknown", c="Unknown", t=0):
        self.__Cin = n
        self.__Nom = m
        self.__Prenom = c
        self.__Tel = t

    def afficher(self):
        print(f"{self.Nom} {self.__Prenom} / CIN : {self.__Cin} / N°TEL : {self.__Tel}")

    @property
    def CIN(self):
        return self.__Cin

    @CIN.setter
    def CIN(self, b):
        self.__Cin = b

    @property
    def Nom(self):
        return self.__Nom

    @Nom.setter
    def Nom(self, b):
        self.__Nom = b

    @property
    def Prenom(self):
        return self.__Prenom

    @Prenom.setter
    def Prenom(self, b):
        self.__Prenom = b

    @property
    def Telephone(self):
        return self.__Tel

    @Telephone.setter
    def Tel(self, b):
        if isinstance(b, int):
            self.__Tel = b


class Compte:
    __count = 0

    def __init__(self, client, s):
        self.__prop = client
        self.__solde = s
        Compte.__count += 1
        self.__code = Compte.__count

    def get_prop(self):
        return self.__prop

    def set_prop(self, p):
        self.__prop = p

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
        if self.__solde >= somme:
            self.__solde -= somme

    def Resumer(self):
        print(
            f"le proprietaire : {self.__prop.Nom } {self.__prop.Prenom} , le numero de compte {self.__code}:  , le solde : {self.__solde}")

    @staticmethod
    def NbCompteCree():
        return Compte.__count


c1 = Client('EE176Y', 'ALAWI', 'Ahmed', 6275378)
c1.afficher()

c2 = Client('EE1zef6Y', 'Kamali', 'mohammed', 62275378)

Compte1 = Compte(c1, 6000)
Compte1.Resumer()
print(c1.Nom)
Compte1.NbCompteCree()

Compte2 = Compte(c1, 100)
Compte2.Resumer()
Compte2.Crediter(200)
Compte2.Resumer()
Compte2.Debiter(50)
Compte2.Resumer()
print(Compte2.NbCompteCree())
