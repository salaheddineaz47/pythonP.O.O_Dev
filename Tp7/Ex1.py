class Stagiaire:
    def __init__(self, cne, name, lastname):
        self.__CNe = cne
        self.__Nom = name
        self.__Prenom = lastname

    def __str__(self):
        return f"{self.__Nom} {self.__Prenom} // CIN : {self.__CNe}"

    @property
    def CNE(self):
        return self.__CNe

    @CNE.setter
    def CNE(self, c):
        self.__CNe = c

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

# ********************************************************


class Groupe:
    def __init__(self, name, fil):
        self.__NomGroup = name
        self.__Filiere = fil
        self.__listeStagiaires = []

    def __str__(self):
        s = ""
        for x in self.__listeStagiaires:
            s += str(x)+"\n"

        if not s:
            s = "Aucun stagiaire dans le groupe"

        return f"* {self.__NomGroup} // Filière : {self.__Filiere} -- \n** Liste de stagiaires : \n{s} "

    @property
    def NomGROUP(self):
        return self.__NomGROUP

    @NomGROUP.setter
    def NomGROUP(self, b):
        self.__NomGROUP = b

    @property
    def Filiere(self):
        return self.__Filiere

    @Filiere.setter
    def Filiere(self, b):
        self.__Filiere = b

    # def RechercherStagCNE(self, cne):
    #     for st in self.__listeStagiaires:
    #         if st.CNE == cne:
    #             print(st)
    #         else:
    #             print(
    #                 f"le stagiaire ayant le {cne} n'existe pas dans le groupe")
    #     if not self.__listeStagiaires:
    #         print("Le groupe ne contient aucun stagiaire")

    def RechercherStagCNE(self, cne):
        c = None
        for st in self.__listeStagiaires:
            if st.CNE == cne:
                print(st)
                c = True
                break
            else:
                c = False

        if not self.__listeStagiaires:
            c = None
        return c

    def ExistStagCNE(self, cne):
        k_list = [x.CNE == cne for x in self.__listeStagiaires]
        k = True in k_list
        return k

    def ExistStagNOM(self, nom, pren):
        k_list = [x.Nom == nom and x.Prenom ==
                  pren for x in self.__listeStagiaires]
        k = True in k_list
        return k

    def AjouterStagCNE(self, cne):
        k_list = [x.CNE == cne for x in self.__listeStagiaires]
        k = True in k_list

        if not k and len(self.__listeStagiaires) <= 25:
            x1 = cne
            x2 = input("Entrez le nom de stagiaire :")
            x3 = input("Entrez le prenom de stagiaire :")
            self.__listeStagiaires.append(Stagiaire(x1, x2, x3))
            print("Le stagiaire a ete ajoute avec succés :")

        else:
            raise Exception(
                "Le CNE deja existant ou le nombre de stagiaires a depassé 25 dans le groupe")

    def AfficherStagCNE(self):
        k = True
        if not self.__listeStagiaires:
            k = False
        if k:
            for x in self.__listeStagiaires:
                print(x)
        return k

    def RetirerStagCNE(self, cne):
        k = False
        for x in self.__listeStagiaires:
            if x.CNE == cne:
                k = True
                self.__listeStagiaires.remove(x)
        return k


st1 = Stagiaire('G121456', 'ALAWI', 'Ahmed')
st2 = Stagiaire('E128156', 'Kamali', 'mohammed')
# print(st1)
# print(st2)
# print(f"--\n--")
gr1 = Groupe("Groupe 1", "DEV")
# print(gr1)
# gr1.AjouterStagCNE("F1652")
# print(gr1)
# gr1.AjouterStagCNE("sk1652")
# print(gr1)

while True:

    print(f"-- 1 -- Rechercher un stagiaire par son CNE dans le groupe. -- \n-- 2 -- Vérifier si un stagiaire spécifique (CNE) existe dans le groupe. --\n-- 3 -- Vérifier si un stagiaire spécifique ( Nom et prénom) existe dans le groupe. --\n-- 4 -- Ajoutez un stagiare au groupe  --\n-- 5 -- Afficher la liste des stagiaires dans le groupe. --\n-- 6 -- Retirer un stagiaire du groupe à partir de son CNE. --\n-- 7 -- Quittez\n")

    while True:
        x = int(input("Entrez le numéro de votre choix : \n"))
        if 1 <= x <= 7:
            break
# ///////////////////////////
    if x == 1:
        cn = input("Entrez le CNE de stagiaire :")

        if gr1.RechercherStagCNE(cn):
            pass
        elif gr1.RechercherStagCNE(cn) == False:
            print(f"le stagiaire ayant le {cn} n'existe pas dans le groupe")
        else:
            print("Le groupe ne contient aucun stagiaire")


# ///////////////////////////
    if x == 2:
        cn = input("Entrez le CNE de stagiaire :")
        if gr1.ExistStagCNE(cn):
            print(f"Le stagiaire ayant le ({cn}) existe dans le groupe ")
        else:
            print(f"Le stagiaire ayant le ({cn}) n'existe pas dans le groupe ")


# ///////////////////////////
    if x == 3:
        n = input("Entrez le nom de stagiaire :")
        p = input("Entrez le prenom de stagiaire :")
        if gr1.ExistStagNOM(n, p):
            print(f"Le stagiaire : ({p},{n}) existe dans le groupe ")
        else:
            print(f"Le stagiaire : ({p},{n}) n'existe pas dans le groupe ")


# ///////////////////////////
    if x == 4:
        cn = input("Entrez le CNE de stagiaire :")
        gr1.AjouterStagCNE(cn)

# ///////////////////////////
    if x == 5:
        if not gr1.AfficherStagCNE():
            print("La liste de stagiaires est vide")

# ///////////////////////////
    if x == 6:
        cn = input("Entrez le CNE de stagiaire :")
        if gr1.RetirerStagCNE(cn):
            print(
                f"Le stagiaire ayant le C.I.N : ({cn}) a ete supprime avec succes")
        else:
            print(
                f"Le stagiaire ayant le C.I.N : ({cn}) n'existe pas dans le groupe")


# ///////////////////////////
    if x == 7:
        print("Vous avez quitter le programme . ")
        break

    c = input("voulez vous continuez (0/N) :")
    if c.lower() != 'o'.lower():
        break
