def search(L, n):
    k = None
    for p in L:
        if p["Nom"] == n:
            k = p
    return k


stock = []

while True:

    print("***********************************************************************")
    print(f"-- 1 -- Ajouter un nouveau produit à la liste avec son nom, son prix unitaire et sa quantité en stock. -- \n-- 2 -- Rechercher un produit en utilisant son nom, et afficher toutes ses informations. --\n-- 3 -- Afficher la liste de tous les produits avec leurs informations. --\n-- 4 -- Mettre à jour les informations d'un produit existant en utilisant son nom.  --\n-- 5 -- Supprimer un produit de la liste en utilisant son nom. --\n-- 6 -- Quitter --\n")

    while True:
        x = int(input("Entrez le numéro de votre choix : "))
        if x in [1, 2, 3, 4, 5, 6]:
            break
# ///////////////////////////
    if x == 1:
        produit = {}
        print(f"Donnez les informations du produit ")

        m = input(f"Donnez le nom du produit : ")
        s = search(stock, m)
        if s is None:
            produit["Nom"] = m
            prix = float(input(f"Donnez le prix du produit : "))
            produit["Prix Unitaire"] = prix
            qt = int(input(f"Donnez la quantité du produit : "))
            produit["Quantite"] = qt
            stock.append(produit)
            print("Le produit a ete ajoute avec succes")
        else:
            print("le produit est deja en stock")

# ///////////////////////////
    if x == 2:
        nom = input("Donnez le nom du produit que vous voulez recherchez : ")

        if search(stock, nom) is None:
            print("Le produit est introuvable")
        else:
            print(search(stock, nom))

# ///////////////////////////
    if x == 3:
        for x in stock:
            print(x)

# ///////////////////////////
    if x == 4:
        nom = input("Donnez le nom du produit que vous voulez modifiez : ")

        s = search(stock, nom)
        if s is None:
            print("Le produit est introuvable")
        else:
            # prix =
            s["Prix Unitaire"] = float(
                input(f"Donnez le nouveau prix du produit : "))
            s["Quantite"] = int(
                input(f"Donnez la nouvelle quantité du produit : "))
            print("Le produit est modifie avec succes")

# ///////////////////////////
    if x == 5:
        nom = input("Donnez le nom du produit que vous voulez supprimez : ")

        s = search(stock, nom)
        if s is None:
            print("Le produit est introuvable")
        else:
            stock.remove(s)
            print("Le produit est supprime")

# ///////////////////////////
    if x == 6:
        print("Vous avez quitter le programme . ")
        break

    c = input("voulez vous continuez (0/N) :")
    if c != 'O' and c != 'o':
        break
