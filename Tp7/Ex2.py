class Client:
    def __init__(self, n, nom, p, ad, t):
        self.__Cin = n
        self.__Nom = nom
        self.__Prenom = p
        self.__Adresse = ad
        self.__Tel = t

    def __str__(self):
        return f"{self.__Nom} {self.__Prenom} / CIN : {self.__Cin} / N°TEL : {self.__Tel}"

    @property
    def CIN(self):
        return self.__Cin

    @CIN.setter
    def CIN(self, b):
        self.__Cin = b

    @property
    def NOM(self):
        return self.__Nom

    @NOM.setter
    def NOM(self, b):
        self.__Nom = b

    @property
    def PRENOM(self):
        return self.__Prenom

    @PRENOM.setter
    def PRENOM(self, b):
        self.__Prenom = b

    @property
    def Telephone(self):
        return self.__Tel

    @Telephone.setter
    def Telephone(self, b):
        self.__Tel = b

    @property
    def Adresse(self):
        return self.__Adresse

    @Adresse.setter
    def Adresse(self, adr):
        self.__Adresse = adr


class Compte:
    __count = 0

    def __init__(self, sol, ty, cli):
        self.__solde = sol
        self.Type = ty
        self.__client = cli
        Compte.__count += 1
        self.__numCompte = Compte.__count

    @property
    def ClienT(self):
        return self.__client

    @ClienT.setter
    def ClienT(self, c):
        self.__client = c

    @property
    def NumCompte(self):
        return self.__numCompte
    # @NumCompte.setter
    # def NumCompte(self,num):

    @property
    def Type(self):
        return self.__type

    @Type.setter
    def Type(self, c):
        if c in ['C', 'E']:
            self.__type = c
        else:
            raise Exception("Le type de compte doit etre C ou E ")

    @property
    def solde(self):
        return self.__solde

    @property
    def code(self):
        return self.__numCompte

    def Crediter(self, somme):
        if somme > 0:
            self.__solde += somme

    def Debiter(self, somme):
        if self.__solde >= somme:
            self.__solde -= somme

    def __str__(self):
        return f"le proprietaire : {self.__client.NOM } {self.__client.PRENOM} , le numero de compte {self.__numCompte}:  , CIN : {self.__client.CIN} le solde : {self.__solde} , Tel : {self.__client.Telephone}"


class Banque:

    def __init__(self, N, s):
        self.__NomBanque = N
        self.__Siege = s
        # self.__ListCompte = []
        self.__ListCompte = [Compte(10, "E", Client("E1", "nom1", "prenom1", "adr1", "077744")), Compte(
            2000, "C", Client("E2", "nom2", "prenom2", "a2", "070944")), Compte(
            2000, "E", Client("E1", "nom1", "prenom1", "a1", "070944"))]

    def __str__(self):
        s = ""
        for x in self.__ListCompte:
            s += str(x)+"\n"
        if not s:
            s = "Aucun Compte se trouve dans la banque"

        return f"La banque : {self.__NomBanque}, le siège : {self.__Siege}\nListe de comptes : \n{s}"

    @property
    def NOMBANQUE(self):
        return self.__NomBanque

    @NOMBANQUE.setter
    def NOMBANQUE(self, s):
        self.__NomBanque = s

    @property
    def Siege(self):
        return self.__Siege

    @Siege.setter
    def Siege(self, s):
        self.__Siege = s

    def RechercherCompte(self, num):
        for cm in self.__ListCompte:
            if cm.NumCompte == num:
                return cm
        return None

    def AjouterCompte(self, compte):
        if compte not in self.__ListCompte:
            self.__ListCompte.append(compte)
            return True
        return False

    def SupprimerCompte(self, num):
        result = self.RechercherCompte(num)

        if result is None:
            return False
        elif (result.solde == 0):
            self.__ListCompte.remove(result)
            return True

    def ModifierTelClient(self, num, tel):
        result = self.RechercherCompte(num)

        if result is None:
            return False
        else:
            result.Client.Telephone = tel
            return True

    def ReturnComptes(self):
        if not self.__ListCompte:
            return None
        return self.__ListCompte

    def ReturnComptesE(self):
        L = []
        k = False
        for compte in self.__ListCompte:
            if compte.Type == "E":
                L.append(compte)
                k = True
        if k:
            return L
        else:
            return None

    def ReturnComptesC(self, minn, maxx):
        if minn > maxx:
            minn, maxx = maxx, minn
        L = []
        if not self.__ListCompte:
            return None
        for compte in self.__ListCompte:
            if minn < compte.solde < maxx:
                L.append(compte)

        return L

    def ReturnComptesCIN(self, cin):
        L = []
        if not self.__ListCompte:
            return None
        for c in self.__ListCompte:
            if c.ClienT.CIN == cin:
                L.append(c)
        return L

    def CompteMax(self):
        L = []
        M = []
        if not self.__ListCompte:
            return None

        for x in self.__ListCompte:
            L.append(x.solde)

        maxx = max(L)
        for c in self.__ListCompte:
            if c.solde == maxx:
                M.append(c)
        return M

        # maxx = self.__ListCompte[0].solde
        # for compte in self.__ListCompte:
        #     if compte.solde > maxx:
        #         maxx = compte.solde
        # k = False
        # for compte in self.__ListCompte:
        #     if compte.solde == maxx:
        #         print(compte)
        #         k = True

        # if not k:
        #     return False
        # else:
        #     return True

    def SommeComptes(self, cin):
        if not self.__ListCompte:
            return None
        s = 0
        k = False
        for compte in self.__ListCompte:
            if compte.ClienT.CIN == cin:
                s += compte.solde
                k = True

        if not k:
            return False
        else:
            return s

    def SommeComptesE(self):
        if not self.__ListCompte:
            return None
        s = 0
        k = False
        for compte in self.__ListCompte:
            if compte.Type == "E":
                s += compte.solde
                k = True

        if not k:
            return False
        else:
            return s

    # def SommeComptesE(self,cin):
    #     if self.ReturnComptesCIN(cin) != None:

        # if not self.__ListCompte:
        #     return None
        # s = 0
        # for compte in self.__ListCompte:
        #     s += compte.solde
        # return s


# C = ClienT("g123", "Nom1", "Prenom1", "adresseeee", "066666")
# print(C)
# cmpt = Compte(2000, "C", C)
# print(cmpt)
# print(cmpt.NumCompte)
# print(b1)

Banque1 = Banque("Banque1", "Siege1")

while True:

    print(f"-- 1 -- Ajouter un compte à la banque. -- \n-- 2 -- Supprimer un compte à partir de son code (si son solde est égal à zéro). --\n-- 3 -- Modifier le numéro de téléphone du client d'un compte donné. --\n-- 4 -- Rechercher un compte à partir de son Numéro.  --\n-- 5 -- Afficher toutes les informations de la banque. --\n-- 6 -- Afficher tous les comptes de la banque. --\n-- 7 -- Afficher tous les comptes d'épargnes de la banque. --\n-- 8 -- Afficher les comptes courants qui ont un solde entre deux valeurs données. --\n-- 9 -- Rechercher le(s) compte(s) à partir de son Client (CIN).  --\n-- 10 -- Afficher la somme de tous les comptes d'épargne de la banque. -- \n-- 11 -- Afficher la somme de tous les comptes d'un client donné (CIN) -- \n-- 12 -- Afficher les comptes ayant le solde maximal. -- \n-- 13 -- Quittez\n")

    while True:
        x = int(input("Entrez le numéro de votre choix : \n"))
        if 1 <= x <= 13:
            break
# ///////////////////////////
    if x == 1:
        sol = float(input("Donnez le solde du compte : "))
        ty = input("Donnez le type de compte :")
        print("Donnez les informations de client :")
        cin = input("Entrez le C.I.N de client ;")
        nom = input("Donnez le nom de client :")
        pre = input("Donnez le prenom de client :")
        adr = input("Donnez l'adresse de client :")
        tel = input("Donnez le telephone de client :")

        client1 = Client(cin, nom, pre, adr, tel)
        c = Compte(sol, ty, client1)
        search = Banque1.AjouterCompte(c)

        if search:
            print("Le compte est ajoute avec succes")
        else:
            print("L'operation a ete echoué")


# ///////////////////////////
    if x == 2:
        numC = int(
            input("Donnez le numero de compte que vous voulez supprimez : "))

        search_result = Banque1.SupprimerCompte(numC)
        if search_result is False:
            print("Le compte que vous voulez supprimé est introuvable")
        else:
            print("Le compte a été supprimé avec succés")


# ///////////////////////////
    if x == 3:
        numt = int(input("Le nouvel numero de Telephone : "))
        cinC = input(
            "Donnez le C.I.N de client que vous voulez modifiez son numero de Telephone : ")

        search_result = Banque1.ModifierTelClient(cinC, numt)

        if search_result:
            print("Le numero de tel a été modifié avec succés")
        else:
            print("Le client est introuvable")


# ///////////////////////////
    if x == 4:
        numC = int(input("Donnez le numero de compte que vous recherchez : "))
        search_result = Banque1.RechercherCompte(numC)

        if search_result is None:
            print("Le compte est introuvable")
        else:
            print(search_result)


# ///////////////////////////
    if x == 5:
        print(Banque1)


# ///////////////////////////
    if x == 6:
        search_result = Banque1.ReturnComptes()
        if search_result is None:
            print("La banque ne contient aucun compte  ")
        else:
            for x in search_result:
                print(x)
            # print(search_result)

# ///////////////////////////
    if x == 7:
        search_result = Banque1.ReturnComptesE()
        if search_result is None:
            print("La banque ne contient pas les comptes d'epargne")
        else:
            for x in search_result:
                print(x)
            # print(search_result)

# ///////////////////////////
    if x == 8:
        mi = float(input("Donnez la valeur minimale :"))
        ma = float(input("Donnez la valeur maximale :"))

        search_result = Banque1.ReturnComptesC(mi, ma)
        if search_result is None:
            print("La banque ne contient aucun compte  ")
        else:
            for x in search_result:
                print(x)
            # print(search_result)


# ///////////////////////////
    if x == 9:
        cin = input("Donnez le CIN de client :")

        search_result = Banque1.ReturnComptesCIN(cin)
        if search_result is None:
            print("La banque ne contient aucun compte  ")
        else:
            for x in search_result:
                print(x)
            # print(search_result)

# ///////////////////////////
    if x == 10:
        search_result = Banque1.SommeComptesE()
        if search_result is None:
            print("La banque ne contient aucun compte : ")
        elif search_result is False:
            print(f"Les comptes d'epargnes n'existent pas dans la banque.  ")
        else:
            print(
                f"La somme des tous les comptes d'epargne est : {search_result}  ")


# ///////////////////////////
    if x == 11:
        cin = input("Donnez le CIN de client :")

        search_result = Banque1.SommeComptes(cin)
        if search_result is None:
            print("La banque ne contient aucun compte ")
        elif search_result is None:
            print(
                f"Le client ayant CIN {cin} n'a aucun compte dans la banque  ")
        else:
            print(
                f"La somme des comptes du client ayant le cin {cin} est :  {search_result}")


# ///////////////////////////
    if x == 12:
        search_result = Banque1.CompteMax()
        if search_result is None:
            print("La banque ne contient aucun compte ")
        else:
            print(
                f"La liste des comptes ayant le solde maximal")
            # print(search_result)
            for x in search_result:
                print(x)


# ///////////////////////////
    if x == 13:
        print("Vous avez quitter le programme . ")
        break

    c = input("voulez vous continuez (0/N) :")
    if c.lower() != 'o'.lower():
        break
