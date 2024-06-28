class Stagiaire:
    def __init__(self, cin, name, lastname, fil, no):
        self.CIN = cin
        self.__Nom = name
        self.__Prenom = lastname
        self.filiere = fil
        self.Note = no

    def __str__(self):
        return f"{self.Nom} {self.__Prenom} / La filière : {self.__filiere} / CIN : {self.__Cin} / La note {self.__Note}  "

    @property
    def CIN(self):
        return self.__Cin

    @CIN.setter
    def CIN(self, b):
        if len(b) == 7 and b[0].isalpha() and b[1:].isdigit():
            self.__Cin = b
        else:
            raise Exception("Le C.I.N est invalide")

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
    def filiere(self):
        return self.__filiere

    @filiere.setter
    def filiere(self, b):
        if b == "DEV" or b == "INFRA":
            self.__filiere = b

    @property
    def Note(self):
        return self.__Note

    @Note.setter
    def Note(self, b):
        if (b >= 0 and b <= 20):
            self.__Note = b
        else:
            raise Exception("la note est invalide")


# L = [Stagiaire('E123456', 'ALAWI', 'Ahmed', 'smp', 20),
#      Stagiaire('E123456', 'Kamali', 'mohammed', 'smp', 16)]

# for p in L:
#     print(p)
L = []
while True:

    print(f"-- 1 -- Affichez tous les stagiares -- \n-- 2 -- Affichez les notes de tous les stagiares --\n-- 3 -- Affichez les stagiare ayant une note superieur ou egale à une note donné --\n-- 4 -- Ajoutez un stagiare dont les informations sont entrés par l'utlisateur  --\n-- 5 -- Recherchez un stagiare par un CIN donné --\n-- 6 --  Recherchez les stagiares d'une filiere donné --\n-- 7 --  Supprimez un stagiare dont le CIN est entré par l'utlisateur --\n-- 8 -- Quittez\n")

    while True:
        x = int(input("Entrez le numéro de votre choix : \n"))
        if x in [1, 2, 3, 4, 5, 6, 7, 8]:
            break
# ///////////////////////////
    if x == 1:
        for p in L:
            print(p)
        if len(L) == 0:
            print(f"La liste ne contient aucun stagiaire \n")

# ///////////////////////////
    if x == 2:
        for i in range(0, len(L)):
            print(
                f"la note du stagiare ayant le CIN : {L[i].CIN} est : {L[i].Note}")
        if len(L) == 0:
            print("La liste ne contient aucune note")

# ///////////////////////////
    if x == 3:
        try:
            x = float(input("Donnez une note : "))
        except ValueError as e:
            print(e)

        for p in L:
            if p.Note >= x:
                print(
                    f"Le stagiare de CIN {p.CIN} a une note {p.Note} superieur à {x}")
        if len(L) == 0:
            print("La liste ne contient aucune note")

# ///////////////////////////
    if x == 4:
        try:
            x1 = input("Donnez le nom du stagiare : ")
            x2 = input("Donnez le prenom du stagiare : ")

            while True:
                x3 = input("Donnez le CIN du stagiare : ")
                ck = True
                for x in L:
                    if x3 == x.CIN:
                        ck = False
                        break

                if ck == False:
                    print("CIN déja existant !! ")

                if ck == True:
                    break

            x4 = input("Donnez la filiere du stagiare : ")
            x5 = float(input("Donnez la note du stagiare : "))
        except ValueError as e:
            print(e)

        L.append(Stagiaire(x3, x1, x2, x4, x5))

# ///////////////////////////
    if x == 5:
        try:
            y = input("Donnez un CIN : ")
            while (len(y) != 7 or not y[0].isalpha() or not y[1:].isdigit()):
                y = input("CIN invalide \n Donnez un CIN : ")
        except ValueError as e:
            print(e)

        j = True
        for p in L:
            if y == p.CIN:
                print(p)
                j = False
                break
        if j:
            print(f"Aucune stagiaire a ce numero de C.I.N {y}")

        if len(L) == 0:
            print("La liste ne contient aucun stagiaire")

# ///////////////////////////
    if x == 6:
        try:
            z = input("Donnez une filiere : ")
        except ValueError as e:
            print(e)

        j = True
        for p in L:
            if z == p.filiere:
                print(p)
                j = False
        if j:
            print(f"Aucune stagiaire n'est dans cette filere : {y}")
        if len(L) == 0:
            print("La liste ne contient aucun stagiaire")

# ///////////////////////////
    if x == 7:
        try:
            c = input("Donnez le CIN du stagiare : ")
            while (len(c) != 7 or not c[0].isalpha() or not c[1:].isdigit()):
                c = input("CIN invalide \n Donnez un CIN : ")
        except ValueError as e:
            print(e)

        j = True
        for p in L:
            if c == p.CIN:
                L.remove(p)
                print(
                    f"Le stagiare qui a le C.I.N {p.CIN} est supprimé avec succés")
                j = False
                break

        if j:
            print(f"Aucune stagiaire ayant ce cin : {c}")


# ///////////////////////////
    if x == 8:
        print("Vous avez quitter le programme . ")
        break

    c = input("voulez vous continuez (0/N) :")
    if c != 'O':
        break

# for p in L:
#     p.Nom = "aaaaaa"
# for o in L:
#     print(o.Nom)
