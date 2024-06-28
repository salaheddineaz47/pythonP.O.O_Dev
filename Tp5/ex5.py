class InvalideCINExeption (Exception):
    pass


class InvalideGradeExeption (Exception):
    pass


class Etudiant:
    def __init__(self, cin, n, p, gr):
        self.CIN = cin
        self.__nom = n
        self.__prenom = p
        self.grade = gr

    def __str__(self):
        return f"le C.I.N : {self.__CIN}, Le nom : {self.__nom}, le prenom : {self.__prenom}, le grade : {self.__grade}"

    @property
    def CIN(self):
        return self.__CIN

    @CIN.setter
    def CIN(self, m):
        if len(m) == 7 and m[0].isalpha() and m[1:].isdigit():
            self.__CIN = m
        else:
            raise InvalideCINExeption("Le C.I.N est invalide")

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, m):
        self.__nom = m

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, m):
        self.__prenom = m

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, g):
        if g == 'A' or g == 'B' or g == 'C' or g == 'D':
            self.__grade = g
        else:
            raise InvalideGradeExeption("Le grade est invalide")


E = Etudiant('g123456', 'Ahmed', "mustafa", "B")
print(E)
# E.grade = "D"
# print(E)
# E.CIN = "S123456"
# print(E)

print("La suite de programme........")
