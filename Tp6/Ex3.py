from classes import Ouvrage, Livre, CD
from operator import attrgetter


def ftprint(L):
    for x in L:
        print(x)


def search(T, n):
    c = None
    for p in T:
        if p.code == n:
            c = p
            break
    return c


Bibliotheque = [Livre("Titre 1", "Auteur 1", "Editeur 1"), Livre("Titre 2", "Auteur 2", "Editeur 2"), CD(
    "CD 1", "Artiste 1", 10), CD("CD 2", "Artiste 2", 12), Livre("Titre 3", "Auteur 2", "Editeur 3")]
Bibliotheque.append(Livre("Titre 3", "Auteur 3", "Editeur 3"))
Bibliotheque.append(Livre("Titre 4", "Auteur 4", "Editeur 4"))
Bibliotheque.append(CD("CD 3", "Artiste 3", 122))
Bibliotheque.append(CD("CD 4", "Artiste 4", 161))
# Bibliotheque[0].NombreEmprunte = 3
# Bibliotheque[1].NombreEmprunte = 2
# Bibliotheque[2].NombreEmprunte = 10
# Bibliotheque = []

while True:
    print("***************************************************************")
    print("\nMenu:")
    print("1. Afficher tous les ouvrages.")
    print("2. Afficher les ouvrages disponibles seulement.")
    print("3. Afficher tous les Livres.")
    print("4. Afficher tous les CDS.")
    print("5. Afficher les auteurs de tous les livres.")
    print("6. Afficher les artistes de tous les CDS.")
    print("7. Ajouter un ouvrage (Livre ou CD) à la bibliothèque.")
    print("8. Supprimer un ouvrage (par code).")
    print("9. Modifier le titre d'un ouvrage.")
    print("10. Rechercher un ouvrage par code. (Afficher également son type)")
    print("11. Rechercher un Livre par code.")
    print("12. Rechercher un CD par code.")
    print("13. Rechercher un ouvrage par titre.")
    print("14. Rechercher un CD par artiste.")
    print("15. Rechercher un Livre par auteur.")
    print("16. Afficher tous les ouvrages classés par type.")
    print("17. Afficher les ouvrages triés par ordre croissant de nombres d'emprunt.")
    print("18. Emprunter un ouvrage par code.")
    print("19. Restituer un ouvrage par code.")
    print("20. Quitter.")

    while True:
        x = int(input("Entrez le numéro de votre choix : "))
        if 0 <= x <= 20:
            break
# ///////////////////////////
    if x == 1:
        # for p in Bibliotheque:
        #     print(p)
        ftprint(Bibliotheque)

        if len(Bibliotheque) == 0:
            print(
                f"La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 2:
        disponibles = [x for x in Bibliotheque if x.Dispo]

        ftprint(disponibles)

        if not disponibles:
            print("Aucun ouvrage disponible dans la bibliotheque.")

        if len(Bibliotheque) == 0:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 3:
        if len(Bibliotheque) != 0:
            livres = [x for x in Bibliotheque if isinstance(x, Livre)]
            ftprint(livres)

            if not livres:
                print("Aucun livre dans la bibliotheque.")

        else:
            print(
                "La bibliotheque ne contient aucun livre !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 4:
        if len(Bibliotheque) != 0:
            cds = [c for c in Bibliotheque if isinstance(c, CD)]
            ftprint(cds)

            if not cds:
                print("Aucun CD dans la bibliotheque.")

        else:
            print(
                "La bibliotheque ne contient aucun CD !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 5:
        if len(Bibliotheque) != 0:

            auteurs = [x.nomAuteur for x in Bibliotheque if isinstance(
                x, Livre) and x.nomAuteur]
            # auteurs = [x for x in Bibliotheque if x not in auteurs]
            ftprint(auteurs)
            if not auteurs:
                print("Aucun auteur dans la bibliotheque.")

        else:
            print(
                "La bibliotheque ne contient aucun article !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 6:
        if len(Bibliotheque) != 0:

            artisteCd = [x.artiste for x in Bibliotheque if isinstance(x, CD)]
            ftprint(artisteCd)

            if not artisteCd:
                print("Aucun artiste dans la bibliotheque.")

        else:
            print(
                "La bibliotheque ne contient aucun article !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 7:
        x1 = input("Donnez le titre de l'ouvrage : ")
        c = input("Entrez le type d'ouvrage (Livre/CD): ").lower()

        if c == "livre":
            x2 = input("Donnez l'auteur du livre : ")
            x3 = input("Donnez l'editeur du livre : ")

            Bibliotheque.append(Livre(x1, x2, x3))
            print("Le livre a été ajouter avec succés.")

        if c == "cd":
            x2 = input("Donnez l'auteur de CD : ")
            x3 = input("Donnez le nombre de pistes : ")

            Bibliotheque.append(CD(x1, x2, x3))
            print("Le CD a été ajouter avec succés.")

        else:
            print("Type d'ouvrage introuvable.")

# ///////////////////////////
    if x == 8:
        if len(Bibliotheque) != 0:

            co = int(
                input("Donnez le code de l'ouvrage que vous voulez supprimez :"))
            c = search(Bibliotheque, co)
            if c == None:
                print("L'ouvrage que vous voulez supprimer est indisponible")
            else:
                Bibliotheque.remove(c)
                print("Ouvrage  a été supprimè avec succés.")

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")


# ///////////////////////////
    if x == 9:
        if len(Bibliotheque) != 0:

            co = int(
                input("Donnez le code de l'ouvrage que vous voulez modifiez :"))

            c = search(Bibliotheque, co)
            if c == None:
                print("L'ouvrage que vous voulez modifier est indisponible")
            else:
                c.titre = input("Entrez le nouvel titre de l'ouvrage: ")
                print("le titre a été modifié avec succes")

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 10:
        if len(Bibliotheque) != 0:

            co = int(input("Donnez le code :"))

            c = search(Bibliotheque, co)
            if c == None:
                print("Ouvrage n'existe pas")
            else:
                print(c)
                if isinstance(c, Livre):
                    print("il sagit d'un livre")
                else:
                    print("il sagit d'un CD")

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 11:
        if len(Bibliotheque) != 0:

            co = int(input("Donnez le code du livre :"))

            c = search(Bibliotheque, co)
            if c == None:
                print("le livre est introuvable")
            elif isinstance(c, Livre):
                print(c)
            else:
                print("ce n'est pas un livre !! il s'agit d'un Cd")

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 12:
        if len(Bibliotheque) != 0:

            co = int(input("Donnez le code de CD :"))

            c = search(Bibliotheque, co)
            if c == None:
                print("le CD est introuvable")
            elif isinstance(c, CD):
                print(c)
            else:
                print("ce n'est pas un CD !! il s'agit d'un livre")

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 13:
        if len(Bibliotheque) != 0:

            T = (input("Donnez le titre de l'ouvrage (Livre/CD) :"))

            k = False

            for p in Bibliotheque:
                if p.titre.lower() == T.lower():
                    print(p)
                    k = True

            if not k:
                print("L'ouvrage est indisponible")

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 14:
        if len(Bibliotheque) != 0:

            nomArt = input("Donnez le nom de lartiste :")

            k = False
            for p in Bibliotheque:
                if isinstance(p, CD) and p.artiste.lower() == nomArt.lower():
                    print(p)
                    k = True

            if not k:
                print("Le CD est indisponible")

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 15:
        if len(Bibliotheque) != 0:

            aut = input("Donnez le nom d'auteur du livre :")

            k = False
            for p in Bibliotheque:
                if isinstance(p, Livre) and p.nomAuteur.lower() == aut.lower():
                    print(p)
                    k = True

            if not k:
                print("Le Livre est indisponible")

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 16:
        if len(Bibliotheque) != 0:

            livres = []
            cds = []

            for o in Bibliotheque:
                if isinstance(o, Livre):
                    livres.append(o)
                else:
                    cds.append(o)

            print("\nLivres:")
            for livre in livres:
                print(livre)

            print("\nCDs:")
            for cd in cds:
                print(cd)

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 17:
        if len(Bibliotheque) != 0:

            # ordered_list = sorted(Bibliotheque, key=attrgetter('NombreEmprunte'))
            ordered_list = sorted(Bibliotheque, key=lambda x: x.NombreEmprunte)

            print("\n  Ouvrages tries par nombre d'emprunts:")
            ftprint(ordered_list)

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")
# ///////////////////////////
    if x == 18:
        if len(Bibliotheque) != 0:
            co = int(input("Donnez le code :"))

            c = search(Bibliotheque, co)

            if c == None:
                print(f"Ouvrage introuvable ")
            else:
                c.Emprunter()

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 19:
        if len(Bibliotheque) != 0:
            co = int(input("Donnez le code :"))

            c = search(Bibliotheque, co)

            if c == None:
                print(f"Ouvrage introuvable ")
            else:
                c.restituer()

        else:
            print(
                "La bibliotheque ne contient aucun ouvrage !! Entrez le choix numero 7 pour l'ajouter \n")

# ///////////////////////////
    if x == 20:
        print("Vous avez quitter le programme . ")
        break

    c = input("voulez vous continuez (0/N) :")
    if c != 'O' and c != 'o':
        break
