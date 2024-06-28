class article:

    def __init__(self, numRef, n, prixV, qt):
        self.numeroReference = numRef
        self.__nom = n
        self.prixVente = prixV
        self.quantiteStock = qt

    def __str__(self):
        return f"L'article : {self.__nom} , le numéro de reference : {self.__numeroReference} , le prix de vente : {self.__prixVente} DH , la quantité en stock : {self.__quantiteStock} "

    @property
    def numeroReference(self):
        return self.__numeroReference

    @numeroReference.setter
    def numeroReference(self, num):
        if isinstance(num, int):
            self.__numeroReference = num
        else:
            raise Exception("le numero de reference doit etre entier")

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, m):
        self.__nom = m

    @property
    def prixVente(self):
        return self.__prixVente

    @prixVente.setter
    def prixVente(self, p):
        if (isinstance(p, int) or isinstance(p, float)) and p > 0:
            self.__prixVente = p
        else:
            raise Exception("le prix doit etre un nombre positif")

    @property
    def quantiteStock(self):
        return self.__quantiteStock

    @quantiteStock.setter
    def quantiteStock(self, qt):
        if isinstance(qt, int) and qt >= 0:
            self.__quantiteStock = qt
        else:
            raise Exception(
                "la quantité doit etre un nombre entier positif ou nulle")


# Articles = [article(1325, "art1", 100, 20), article(
#     12225, "art2", 50, 200), article(67225, "art3", 160, 180)]
Articles = []
while True:

    print("***********************************************************************")
    print(f"-- 1 -- Affichez tous les articles -- \n-- 2 -- Affichez les articles en rupture de stock --\n-- 3 -- Rechercher un article par référence --\n-- 4 -- Rechercher un article par nom  --\n-- 5 -- Rechercher un article par intervalle de prix de vente --\n-- 6 --  Vérifier la disponibilité d'un article --\n-- 7 --  Ajouter un article en stock --\n-- 8 -- Supprimer un article par référence --\n-- 9 -- Modofier un article par référence --\n-- 10 -- Quitter --\n")

    while True:
        x = int(input("Entrez le numéro de votre choix : "))
        if x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            break
# ///////////////////////////
    if x == 1:
        for p in Articles:
            print(p)
        if len(Articles) == 0:
            print(
                f"La liste ne contient aucun article !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 2:
        cmp = False
        for p in Articles:
            if p.quantiteStock == 0:
                print(
                    f"L'article {p.nom} de référence {p.numeroReference} est actuellement indisponible")
                cmp = True

        if not cmp:
            print("Acun article n'est en rupture de stock.")
        if len(Articles) == 0:
            print(
                "La liste ne contient aucun article !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 3:
        if len(Articles) != 0:
            try:
                ref = int(
                    input("Donnez la référence de l'article que vous chercher : "))
            except ValueError as e:
                print(e)

            cmp = False
            for p in Articles:
                if ref == p.numeroReference:
                    print(
                        f"L'artice que vous cherchez est disponible, voila ses informations : ")
                    print(p)
                    cmp = True
            if not cmp:
                print("L'artice que vous chercher est indisponible")

        else:
            print(
                "La liste ne contient aucun article !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 4:
        if len(Articles) != 0:
            try:
                ar = input("Donnez la nom de l'article que vous chercher : ")
            except ValueError as e:
                print(e)

            cmp = False
            for p in Articles:
                if ar == p.nom:
                    print(
                        f"L'artice que vous cherchez est disponible, voila ses informations : ")
                    print(p)
                    cmp = True
            if not cmp:
                print("L'artice que vous chercher est indisponible")

        else:
            print(
                "La liste ne contient aucun article !! Entrez le choix numero 7 pour l'ajouter \n")


# ///////////////////////////
    if x == 5:
        if len(Articles) != 0:
            try:
                a = float(input("Donnez le prix minimal de vente : "))
                b = float(input("Donnez le prix maximal de vente : "))
            except ValueError as e:
                print(e)

            if a > b:
                a, b = b, a

            cmp = False
            for o in Articles:
                if o.prixVente >= a and o.prixVente <= b:
                    print(
                        f"L'article(s) ayant le prix dans l'intervalle prix [{a} , {b}] : \n")
                    print(o)
                    cmp = True
            if not cmp:
                print("L'artice que vous chercher est indisponible")

        else:
            print(
                "La liste ne contient aucun article !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 6:
        if len(Articles) != 0:
            try:
                ref = int(input("Donnez le numero de référence d'un article : "))
            except ValueError as e:
                print(e)

            cmp = False
            for p in Articles:
                if ref == p.numeroReference:
                    print(
                        f"L'article {p.nom} de numero de référence {p.numeroReference} est disponible")
                    cmp = True
                    break

            if not cmp:
                print("L'artice que vous chercher est indisponible")

        else:
            print(
                "La liste ne contient aucun article !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 7:
        try:

            while True:
                x1 = int(input("Donnez le numero de référence d'un article : "))
                ck = True
                for x in Articles:
                    if x1 == x.numeroReference:
                        ck = False
                        break

                if not ck:
                    print(f"numero de référence {x1} est déja existant !! ")

                if ck:
                    break

            x2 = input("Donnez le nom d'un article : ")

            x3 = float(input("Donnez le prix de vente : "))
            x4 = int(input("Donnez la quantité en stock : "))

        except Exception as e:
            print(e)

        Articles.append(article(x1, x2, x3, x4))
        print("L'artcle a été ajouté avec succés.")

# ///////////////////////////
    if x == 8:
        if len(Articles) != 0:
            try:
                ref = int(
                    input("Donnez le numero de référence de l'article que vous voulez supprimer : "))
            except ValueError as e:
                print(e)

            cmp = False
            for p in Articles:
                if ref == p.numeroReference:
                    Articles.remove(p)
                    print("L'artcle a été supprimè avec succés.")
                    cmp = True
                    break
            if not cmp:
                print("L'artice que vous voulez supprimer est indisponible")

        else:
            print(
                "La liste ne contient aucun article !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 9:
        if len(Articles) != 0:
            try:
                ref = int(
                    input("Donnez le numero de référence de l'article que vous voulez modifiez : "))
            except ValueError as e:
                print(e)

            cmp = False
            for p in Articles:
                if ref == p.numeroReference:
                    p.nom = input("Donnez un nouvel nom de l'article : ")
                    p.prixVente = float(
                        input("Donnez un nouvel prix de vente de l'article : "))
                    p.quantiteStock = int(
                        input("Donnez la nouvelle quantité en stock de l'article : "))

                    print("L'artcle a été modifié avec succés.")
                    ck = True
                    break

            if not cmp:
                print("L'artice que vous voulez modifier est indisponible")

        else:
            print(
                "La liste ne contient aucun article !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 10:
        print("Vous avez quitter le programme . ")
        break

    c = input("voulez vous continuez (0/N) :")
    if c != 'O' and c != 'o':
        break
