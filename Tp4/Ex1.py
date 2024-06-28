from abc import ABC, abstractmethod


class Media(ABC):
    def __init__(self, t=" ", e=None):
        self.__titre = t
        self.__emprunte = e

    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, t):
        self.titre = t

    @property
    def emprunte(self):
        return self.__emprunte

    @emprunte.setter
    def emprunte(self, t):
        if isinstance(t, bool):
            self.__emprunte = t

    def etatEmprunte(self):
        if self.__emprunte == True:
            return f" est emprunté"
        else:
            return f" n'est pas emprunté"

    def __str__(self):
        return f": {self.etatEmprunte()} ,le titre est : {self.__titre} "

    @abstractmethod
    def Emprunter():
        pass

    @abstractmethod
    def retourner():
        pass


class Livre(Media):
    def __init__(self, t=" ", e=None, a="", g=""):
        super().__init__(t, e)
        self.__auteur = a
        self.__genre = g

    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, t):
        self.auteur = t

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, t):
        self.genre = t

    def __str__(self):
        return f"L'auteur est {self.auteur} ,le genre est {self.genre} , le livre" + super().__str__()

    def Emprunter(self):
        if self.emprunte == True:
            self.emprunte = False
            return f"Le livre ({self.titre},{self.__auteur}) a été emprunté avec succès"

    def retourner(self):
        if self.emprunte == False:
            self.emprunte = True
            return f"Le livre ({self.titre},{self.__auteur}) a été restitué avec succès"


class CD(Media):
    def __init__(self, t=" ", e=None, artist="", duree=""):
        super().__init__(t, e)
        self.__nomArtiste = artist
        self.__duree = duree

    @property
    def nomArtiste(self):
        return self.__nomArtiste

    @nomArtiste.setter
    def nomArtiste(self, name):
        if isinstance(name, str):
            self.nomArtiste = name

    @property
    def duree(self):
        return self.__duree

    @duree.setter
    def duree(self, d):
        if isinstance(d, str):
            self.duree = d

    def __str__(self):
        return f"L'artiste est {self.__nomArtiste} , la durre est : {self.duree} ,le cd " + super().__str__()

    def Emprunter(self):
        if self.emprunte == True:
            self.emprunte = False
            return f"Le CD ({self.titre},{self.nomArtiste}) a été emprunté avec succès"

    def retourner(self):
        if self.emprunte == False:
            self.emprunte = True
            return f"Le livre ({self.titre},{self.nomArtiste}) a été restitué avec succès"


# livre1 = Livre('titr1', True, "Auteur", "pdf")
# print(livre1)
# print(livre1.auteur, livre1.genre, livre1.titre, livre1.emprunte)
# print(livre1.Emprunter())
# print(livre1)
# print(livre1.retourner())
# print(livre1)

cd1 = CD('titrecd', True, "Artiste", 10)
print(cd1)
print(cd1.nomArtiste, cd1.duree, cd1.titre, cd1.emprunte)
print(cd1.Emprunter())
print(cd1)
print(cd1.retourner())
print(cd1)
