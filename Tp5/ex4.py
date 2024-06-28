class Etudiant:
    def __init__(self, n, a, moy):
        self.__nom = n
        self.age = a
        self.moyenne = moy

    def __str__(self):
        return f"Le nom : {self.__nom}, l'age : {self.__age}, la moyenne : {self.__moyenne}"

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, m):
        self.nom = m

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, a):
        if isinstance(a, int) and a >= 18 and a <= 26:
            self.__age = a
        else:
            raise Exception("L'age doit etre entre 18 et 26")

    @property
    def moyenne(self):
        return self.__moyenne

    @moyenne.setter
    def moyenne(self, a):
        if (isinstance(a, float) or isinstance(a, int)) and a >= 0 and a <= 20:
            self.__moyenne = a
        else:
            raise Exception("L'moyenne doit etre entre 0 et 20")


print("La suite de programme........")

E = Etudiant('Ahmed', 18, 20)
print(E)
