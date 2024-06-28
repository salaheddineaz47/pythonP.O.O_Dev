class Livre:
    def __init__(self, aut="Unknown", t="title unknown", a=None, d=None):
        self.__auteur = aut
        self.__titre = t
        self.__annedepub = a
        self.__disponiblelivre = d

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, a):
        self.__auteur = a

    def get_titre(self):
        return self.__titre

    def set_titre(self, t):
        self.__titre = t

    def get_annedepub(self):
        return self.__annedepub

    def set_annedepub(self, p):
        self.__annedepub = p

    def get_disponiblelivre(self):
        return self.__disponiblelivre

    def set_disponiblelivre(self, p):
        if isinstance(p, bool):
            self.__disponiblelivre = p

    def checkdispo(self):
        if self.__disponiblelivre:
            return "est displonible"
        else:
            return "n'est pas disponible"

    def emprunter(self):
        if self.__disponiblelivre:
            print("le livre est emprunte avec succes")
            self.__disponiblelivre = False

    def rendre(self):
        if self.__disponiblelivre == False:
            self.__disponiblelivre = True
            print("le livre est rendu avec succes")

    def __str__(self):
        return f"l'auteur du Livre titulé {self.__titre} est {self.__auteur}, L'année de publication: {self.__annedepub}, le livre est-il disponible : {self.checkdispo()}, "


class LivreNumerique(Livre):
    def __init__(self, aut="Unknown", t="title unknown", a=None, d=None, f=""):
        super().__init__(aut, t, a, d)
        self.__format = f
        # self.__telecharger = False

    def get_format(self):
        return self.__format

    def set_format(self, p):
        self.__format = p

    def telecharger(self):
        print("telechargement en cours...")
        print("telechargement termine!")

    def convertir_format(self, newformat):
        print(
            f"Conversion de {self.get_titre()} de {self.__format} vers {newformat} en cours...")
        self.__format = newformat
        print(f"convertee correctement au format {newformat}")

    def __str__(self):
        return super().__str__() + f"de format : {self.__format}"


# Livre = Livre("Victor Hugo", "Les misérables", 2000, True)
# Livre.emprunter()
# print(Livre)
# Livre.rendre()
# print(Livre)
LivreNum = LivreNumerique("The author", 'The book', 2010, True, 'mp4')
print(LivreNum)
LivreNum.telecharger()
LivreNum.convertir_format('pdf')
print(LivreNum)
