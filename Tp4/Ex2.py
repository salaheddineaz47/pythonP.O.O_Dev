from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Employe(ABC):
    def __init__(self, m="", n="", p="", birthd=""):
        self.__matricule = m
        self.__nom = n
        self.__prenom = p
        self.__dateDeNaissance = datetime.strptime(birthd, "%Y-%m-%d")

    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, m):
        self.matricule = m

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, n):
        self.nom = n

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, n):
        self.prenom = n

    @property
    def dateDeNaissance(self):
        return self.__dateDeNaissance

    @dateDeNaissance.setter
    def dateDeNaissance(self, dateN):
        self.dateDeNaissance = datetime.strptime(dateN, "%Y-%m-%d")

    def __str__(self):
        return f"Le matricule est {self.__matricule}, le nom : {self.__nom}, le prenom : {self.prenom}, date de naissance : {self.dateDeNaissance}"

    @abstractmethod
    def GetSalaire():
        pass


class Ouvrier(Employe):
    __smig = 3000

    def __init__(self, m="", n="", p="", birthd="", dateentr=int):
        super().__init__(m, n, p, birthd)
        self.__DateEntree = datetime.strptime(dateentr, "%Y-%m-%d").date()

    def __str__(self):
        return super().__str__() + f"La date d'entree est {self.__DateEntree}"

    @property
    def DateEntree(self):
        return self.__DateEntree

    @DateEntree.setter
    def DateEntree(self, dateEntr):
        datetime.strptime(dateEntr, "%Y-%m-%d")

    @staticmethod
    def get_smig():
        return Ouvrier.__smig

    @staticmethod
    def set_smig(s):
        Ouvrier.__smig = s

    def GetSalaire(self):
        ancienete = datetime.now().year - self.__DateEntree.year
        salaire = Ouvrier.__smig + ancienete * 100
        if salaire > Ouvrier.__smig*2:
            salaire = Ouvrier.__smig*2

        return min(salaire, Ouvrier.__smig * 2)


class Cadre(Employe):
    def __init__(self, m="", n="", p="", birthd="", ind=None):
        super().__init__(m, n, p, birthd)
        self.__indice = ind
        # self.__salaire = None

    def __str__(self):
        return super().__str__() + f"L'indice' est {self.__indice}"

    def get_indice(self):
        return self.__indice

    def set_indice(self, indice):
        self.__indice = indice

    def GetSalaire(self):
        if self.__indice == 1:
            return 130000
        elif self.__indice == 2:
            return 150000
        elif self.__indice == 3:
            return 170000
        elif self.__indice == 4:
            return 200000


class Patron (Employe):
    __chiffre_affaires = None

    def __init__(self, m="", n="", p="", birthd="", pourcentage=None):
        super().__init__(m, n, p, birthd)
        self.__pourcentage = pourcentage

    def get_chiffre_affaires(self):
        return Patron.__chiffre_affaires

    def set_chiffre_affaires(self, chiffre_affaires):
        self.chiffre_affaires = chiffre_affaires

    def get_pourcentage(self):
        return self.__pourcentage

    def set_pourcentage(self, pourcentage):
        self.__pourcentage = pourcentage

    def GetSalaire(self):
        return (Patron.__chiffre_affaires * self.__pourcentage) / 100


ouvrier1 = Ouvrier("123", "Dupont", "Jean", "1980-01-01", "2010-01-01")
print(ouvrier1)
print(f"Salaire ouvrier: {ouvrier1.GetSalaire()} DH")
