# stock = []
stock = [{"Nom": "Nom1", "Prix Unitaire": 200, "Quantite": 102},
         {"Nom": "Nom2", "Prix Unitaire": 70, "Quantite": 120}]


def search(L, n):
    k = None
    for p in L:
        if p["Nom"].upper() == n.upper():
            k = p
    return k


def printProduits(L):
    for i in range(0, len(L)):
        print(L[i])


while True:

    while True:
        print(f" Menu: \n 1: Ajouter un nouveau produit à la liste avec son nom, son prix unitaire et sa quantité en stock.  \n 2: Rechercher un produit en utilisant son nom, et afficher toutes ses informations. \n 3: Afficher la liste de tous les produits avec leurs informations. \n 4: Mettre à jour les informations d'un produit existant en utilisant son nom.  \n 5: Supprimer un produit de la liste en utilisant son nom. \n 6: Quitter \n")
        x = int(input("Entrez le numéro de votre choix : "))

        if x == 1:
            produit = {}
            print(f"Donnez les informations du produit ")
            m = input(f"Donnez le nom du produit : ")

            if search(stock, m) == None:

                produit["Nom"] = m
                prix = float(input(f"Donnez le prix du produit : "))
                produit["Prix Unitaire"] = prix
                qt = int(input(f"Donnez la quantite du produit : "))
                produit["Quantite"] = qt
                stock.append(produit)
                print("Le produit a ete ajoute avec succes")
            else:
                print("ce produit existe deja dans le Stock")

        elif x == 2:
            nom = input(
                "Donnez le nom du produit que vous voulez recherchez : ")

            if search(stock, nom) is None:
                print("Le produit est introuvable")
            else:
                print(search(stock, nom))

        elif x == 3:
            printProduits(stock)

        elif x == 4:
            nom = input("Donnez le nom du produit que vous voulez modifiez : ")

            s = search(stock, nom)
            if s is None:
                print("Le produit est introuvable")
            else:
                prix = float(input(f"Donnez le nouveau prix du produit : "))
                s["Prix Unitaire"] = prix
                qt = int(input(f"Donnez la nouvelle quantité du produit : "))
                s["Quantite"] = qt
                print("Le produit est modifie avec succes")

        elif x == 5:
            nom = input(
                "Donnez le nom du produit que vous voulez supprimez : ")

            s = search(stock, nom)
            if s is None:
                print("Le produit est introuvable")
            else:
                stock.remove(s)
                print("Le produit est supprime")

        elif x == 6:
            print("Vous avez quitter le programme . ")
            break
        else:
            print("chiox invalide")
        c = input("voulez vous continuez (0/N) :")
        if c != 'O' and c != 'o':
            break
