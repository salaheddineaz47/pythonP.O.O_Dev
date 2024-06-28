class Personne:
    def __init__(self, n, a):
        self.__nom = n
        self.__age = a

    def get_nom(self):
        return self.__nom

    def set_nom(self, n):
        self.__nom = n

    def get_age(self):
        return self.__age

    def set_age(self, a):
        self.__age = a

    def afficher_infos(self):
        print(f"Je m'appelle , {self.__nom} et j'ai {self.__age} ans", end=" ")


class Etudiant(Personne):
    def __init__(self, n, a, f):
        super().__init__(n, a)
        self.__filiere = f

    def get_filiere(self):
        return self.__filiere

    def set_filiere(self, a):
        self.__filiere = a

    def afficher_infos(self):
        super().afficher_infos()
        print(f"ma filiere est : {self.__filiere}")


P1 = Personne('khalid', 22)
P1.afficher_infos()
print("\n")

E1 = Etudiant('ahemd', 25, 'Dep1')
E1.afficher_infos()


class Employe(Personne):
    def __init__(self, n, a, p):
        super().__init__(n, p, a)
        self.poste = p

    def get_poste(self):
        return self.__poste

    def set_poste(self, p):
        self.__poste = p

    def afficher_infos(self):
        super().afficher_infos()
        print("et j'ocuupe le poste", self.__poste)


Emp = Etudiant('Ali', 25, 'Directeur')
Emp.afficher_infos()
