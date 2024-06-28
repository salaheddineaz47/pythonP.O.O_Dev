from abc import ABC, abstractmethod


class Ouvrage(ABC):
    __codecmp = 0

    def __init__(self, titre):
        self.__titre = titre
        self.__dispo = True
        self.__nombre_emprunts = 0
        Ouvrage.__codecmp += 1
        self.__code = Ouvrage.__codecmp

    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, t):
        self.__titre = t

    @property
    def code(self):
        return self.__code

    @property
    def NombreEmprunte(self):
        return self.__nombre_emprunts

    @NombreEmprunte.setter
    def NombreEmprunte(self, t):
        self.__nombre_emprunts = t

    @property
    def Dispo(self):
        return self.__dispo

    # @Dispo.setter
    # def Dispo(self, t):
    #     self.__dispo = t

    def etatDispo(self):
        pass

    @abstractmethod
    def Emprunter(self):
        pass

    @abstractmethod
    def restituer(self):
        pass

    def __str__(self):
        return f"Etat :{self.etatDispo()} // Code: {self.__code}, // Titre: {self.__titre} // Nombre d'emprunts: {self.__nombre_emprunts}"


class Livre(Ouvrage):
    def __init__(self, titre, auteur, editeur):
        super().__init__(titre)
        self.__nomAuteur = auteur
        self.__nomEditeur = editeur
        self.NombreEmprunte = 0

    @property
    def nomAuteur(self):
        return self.__nomAuteur

    @nomAuteur.setter
    def nomAuteur(self, t):
        self.__nomAuteur = t

    @property
    def nomEditeur(self):
        return self.__nomEditeur

    @nomEditeur.setter
    def nomEditeur(self, t):
        self.__nomEditeur = t

    def etatDispo(self):
        if self.Dispo:
            return f"Le livre est disponible."
        else:
            return f"Le livre est déja emprunté."

    def Emprunter(self):
        if self.Dispo:
            self.Dispo = False
            self.NombreEmprunte += 1
            print(
                f"Le livre ({self.titre}, {self.__nomAuteur}) a été emprunté avec succès.")
        else:
            print("le livre est déja emprunté")

    def restituer(self):
        if not self.Dispo:
            self.Dispo = True
            print(
                f"Le livre ({self.titre}, {self.__nomAuteur}) a été restitué avec succès.")
        else:
            print("Le livre est déja à la bibliotheque")

    def __str__(self):
        return super().__str__() + f"// Auteur: {self.__nomAuteur}// Editeur: {self.__nomEditeur} \n ***************************************************"


class CD(Ouvrage):
    def __init__(self, titre, artiste, nb_piste):
        super().__init__(titre)
        self.__artiste = artiste
        self.__nombre_pistes = nb_piste
        self.NombreEmprunte = 0

    @property
    def artiste(self):
        return self.__artiste

    @artiste.setter
    def artiste(self, t):
        self.__artiste = t

    def etatDispo(self):
        if self.Dispo:
            return f"Le CD est disponible."
        else:
            return f"Le CD est déja emprunté."

    def Emprunter(self):
        if self.Dispo:
            self.Dispo = False
            self.NombreEmprunte += 1
            print(
                f"Le CD ({self.titre}, {self.__artiste}) a été emprunté avec succès.")
        else:
            print(f"Le CD est déja emprunté")

    def restituer(self):
        if not self.Dispo:
            self.Dispo = True
            print(
                f"Le CD ({self.titre}, {self.__artiste}) a été restitué avec succès.")
        else:
            print("Le CD est déja à la bibliotheque")

    def __str__(self):
        return super().__str__() + f"// Artiste: {self.__artiste}// Nombre de pistes: {self.__nombre_pistes} \n ***************************************************"


# livre1 = Livre("Titre 1", "Auteur 1", "Editeur 1")
# livre2 = Livre("Titre 2", "Auteur 2", "Editeur 2")

# cd1 = CD("Titre CD 1", "Artiste 1", 10)


# cd2 = CD("Titre CD 2", "Artiste 2", 12)

# print(livre1)
# livre1.Emprunter()
# print(livre1)

# livre1.restituer()
# livre1.Emprunter()
# print(livre1)
# print(livre2)
# print(cd1)
# print(cd2)

# livre1.Emprunter()
# print(livre1)
# livre1.restituer()
# print(livre1)
# Bibliotheque = [CD("Titre CD 1", "Artiste 1", 10), Livre(
#     "Titre Livre 2", "Auteur 2", "Editeur 2")
