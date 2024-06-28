class Employe:
    def __init__(self, n, s):
        self.__nom = n
        self.__salaire = s
        # self.set_salaire(s)

    def get_nom(self):
        return self.__nom

    def set_nom(self, p):
        self.__nom = p

    def get_salaire(self):
        return self.__salaire

    def set_salaire(self, s):
        if s > 0 and isinstance(s, float):
            self.__salaire = s

    def afficher_infos(self):
        print(
            f"Je m'appelle {self.__nom} , mon salaire est {self.__salaire} ", end=' ')

    def calculer_salaire_annuel(self):
        return self.__salaire*12

    def __str__(self):
        return f" le nom :{self.__nom}, le salaire : {self.__salaire}"


class Directeur(Employe):
    def __init__(self, n, s, p, na):
        super().__init__(n, s)
        self.__prime = p
        self.__nbactions = na

    def get_prime(self):
        return self.__prime

    def set_prime(self, p):
        self.__prime = p

    def get_nbactions(self):
        return self.__nbactions

    def set_nbactions(self, p):
        self.__nbactions = p

    def afficher_infos(self):
        super().afficher_infos()
        print(
            f"et j'ai un prime de {self.__prime}, et j'execute {self.__nbactions} taches")

    def calculer_salaire_annuel(self):
        salaire = super().calculer_salaire_annuel() + self.__prime
        return salaire

    def __str__(self):
        return super().__str__() + f" le prime :{self.__prime}, le nb d'actions : {self.__nbactions}"


Emp = Employe('Mohammed', 1000)
Emp.afficher_infos()
print("\n")
print(f"le salaire annuel de {Emp.get_nom()} ", Emp.calculer_salaire_annuel())
print(Emp)
D = Directeur('Ahmed', 2000, 500, 5)
D.afficher_infos()
print(f"le salaire  annuel de {D.get_nom()} ", D.calculer_salaire_annuel())
print(D)
