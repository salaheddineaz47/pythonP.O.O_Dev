from abc import ABC,abstractmethod

class Ouvrage(ABC):
    __counter = 0
    def __init__(self,t,):
        self.__titre = t
        Ouvrage.__counter += 1
        self.__code = Ouvrage.__counter
        self.__nbremprunter = 0
        self.__etat = True
    
    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self,t):
        self.__titre = t

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self,c):
        self.__code = c
    
    @property
    def nombre_emprunter(self):
        return self.__nbremprunter
    @nombre_emprunter.setter
    def nombre_emprunter(self,nbr):
        self.__nbremprunter = nbr
    
    @property
    def etat(self):
        return self.__etat
    @etat.setter
    def etat(self,c):
        self.__etat = c
    
    @abstractmethod
    def Emprunter():
        pass
    def Restituer():
        pass
    
    def __str__(self):
        return f"Le code {self.__code} le nombre d'emprunter est {self.nombre_emprunter} et le titre est {self.__titre}, "

class Livre(Ouvrage):
    def __init__(self, t, a, e):
        super().__init__(t)
        self.__auteur = a
        self.__editeur = e
    
    @property
    def auteur(self):
        return self.__auteur
    @auteur.setter
    def auteur(self,a):
        self.__auteur = a
    
    @property
    def editeur(self):
        return self.__editeur
    @editeur.setter
    def editeur(self,e):
        self.__editeur = e
    
    def Emprunter(self):
        if self.etat:
            self.nombre_emprunter += 1
            self.etat = False
            print(f"Le livre {self.titre},{self.auteur} a ete emprunte avec succes.")
        else:
            print("Le livre n'est pas disponible pour emprunter.")
    
    def Restituer(self):
        if self.etat != True:
            self.etat = True
            print(f"Le livre {self.titre},{self.auteur} a ete restitue avec succes.")
        else:
            print("Le livre a deja restitue.")
    
    def __str__(self):
        return super().__str__() + f"l'auteur est {self.auteur}, l'editeur est {self.editeur}"

class CD(Ouvrage):
    def __init__(self, t, a, p):
        super().__init__(t)
        self.__artiste = a
        self.__pistes = p

    @property
    def artiste(self):
        return self.__artiste
    @artiste.setter
    def artiste(self,a):
        self.__artiste = a
    
    @property
    def pistes(self):
        return self.__pistes
    @pistes.setter
    def pistes(self,p):
        self.__pistes = p
    
    def Emprunter(self):
        if self.etat:
            self.nombre_emprunter += 1
            self.etat = False
            print(f"Le CD {self.titre},{self.artiste} a ete emprunter avec succes.")
        else:
            print("Le CD n'est pas disponible pour emprunter.")
        
    def Restituer(self):
        if self.etat != True:
            self.etat = True
            print(f"Le CD {self.titre},{self.artiste} a ete restituer avec succes.")
        else:
            print("Le CD est deja restitue.")
    
    def __str__(self):
        return super().__str__() + f"l'artiste est {self.artiste}, le nombre de piste est {self.pistes}."


T = [Livre('livre1','auteur1','editeur1'),CD('cidi2','artist2',2),Livre('livre2','auteur2','editeur2'),Livre('livre3','auteur3','editeur3'),Livre('livre4','auteur4','editeur4'),CD('cidi1','artist1',1),CD('cidi3','artist3',3),CD('cidi4','artist4',4)]

def search(T,n):
    c = None
    for p in T:
        if p.code == n:
            c = p
            break
    return c




while True:
    print("""

    1.Afficher tous les ouvrages.

    2.Afficher les ouvrages disponibles
        
    3.Afficher tous les Livres.
    
    4.Afficher tous les CDs.
    
    5.Afficher tous les auteurs de tous les livres.
    
    6.Afficher les artistes de tous les CDs.
          
    7.Ajouter un ouvrage livre ou CD a la bibliotheque.
    
    8.Supprimer un ouvrage par code.
    
    9.Modifier le titre d'un ouvrage.       

    10.Rechercher un ouvrage par code.

    11.Rechercher un livre par code.

    12.Rchercher un CD par code.

    13.Rchercher un ouvrage par titre.

    14.Rchercher un CD par artiste.

    15.Rchercher un Livre par auteur.

    16.Afficher tous les ouvrages classes par type.

    17.Affchire les ouvrages tries par ordre croissant de numbrose d'emprunt.     

    18.Emprunter un ouvrage par code.
          
    19.Restituer un ouvrage par code.
          
    20.Quitter
        """)

    x = int(input())

    if x == 1:
        [print(p) for p in T]

    
    elif x == 2:
        c = [p for p in T if p.etat]
        # if c:
        #     [print(p) for p in c]
        # else:
        #     print("Aucun ouvrage n'est disponible")

        [print(p) for p in c] if c else print("Aucun ouvrage n'est disponible")


    elif x == 3:
        c = [p for p in T if isinstance(p,Livre)]
        # if c:
        #     [print(p) for p in c]
        # else:
        #     print("Aucun livre trouve")

        [print(p) for p in c] if c else print("Aucun livre trouve")
    
    elif x == 4:
        c = [p for p in T if isinstance(p,CD)]
        # if c:
        #     [print(p) for p in c]
        # else:
        #     print("Aucun CD trouve")

        [print(p) for p in c] if c else print("Aucun CD trouve")            

    elif x == 5:
        c = [p for p in T if isinstance(p,Livre)]
        # if c:
        #     [print(p.auteur) for p in c]
        # else:
        #     print("Aucun auteur trouve")

        [print(p.auteur) for p in c] if c else print("Aucun auteur trouve")
    
    elif x == 6:
        c = [p for p in T if isinstance(p,CD)]
        # if c:
        #     [print(p.artiste) for p in c]
        # else:
        #     print("Aucun artiste est trouve")

        [print(p.artiste) for p in c] if c else print("Aucun artiste est trouve")
    
    elif x == 7:
        select = int(input("Ajouter un ouvrage livre (1) ou CD (2): "))
        if select == 1:
            T.append(Livre(input("Donner le titre du livre: "),input("Donner le nom d'auteur: "),input("Donner le nom d'editeur: ")))
        elif select == 2:
            T.append(CD(input("Donner le titre du CD: "),input("Donner l'artiste du CD: "),int(input("Donner le nombre de piste de CD: "))))
        else:
            raise ValueError("Choix invalid")

        print("Ouvrage ajouter avec success")
        

    elif x == 8:
        code = int(input("Donner le code d'ouvrage: "))
        c = search(T,code)

        # if c == None:
        #     print("Code n'exist pas")
        # else:
        #     T.remove(c)
        #     print("ouvrage supprimer")
        [print("code n'exist pas") if c is None else T.remove(c) and print("ouvrage supprimer")]


    elif x == 9:
        code = int(input("Donner le code d'ouvrage: "))
        c = search(T,code)
        # if c is None:
        #     print("Code n'exist pas")
        # else:
        #     c.titre = input("Donner le nouveau titre: ")
        #     print("ouvrage modifier")
        
        c.titre = input("doner le nouveau titre: ") and print("ouvrage modifier") if c is not None else print("code n'exist pas")


    elif x == 10:
        code = int(input("Donner le code d'ouvrage: "))
        c = search(T,code)
        if c is None:
            print("Code n'exist pas")
        else:
            type = 'livre' if isinstance(c,Livre) else 'CD'

            print(f"L'ouvrage est {c.titre} et son type est {type}.")

    
    elif x == 11:
        code = int(input("Donner le code de livre: "))
        c = search(T,code)
        
        # if c == None or isinstance(c,CD):
        #     print("Aucun livre exist dans ce code")
        # else:
        #     print(c)

        [print("Aucun livre exist dans ce code") if c == None or isinstance(c,Livre) else print(c)]

    elif x == 12:
        code = int(input("Donner le code de CD: "))
        c = search(T,code)
        # if c == None or isinstance(c,Livre):
        #     print("Auncune CD exist dans ce code")
        # else:
        #     print(c)

        [print("Auncune CD exist dans ce code") if c is None or isinstance(c,CD) else print(c)]

    elif x == 13:
        tit = input("Donner le titre d'ouvrage: ")
        c = [p for p in T if p.titre.lower() == tit.lower()]
        # if c:
        #     [print(p) for p in c]
        # else:
        #     print("ouvrage n'exist pas")

        [print(p) for p in c] if c else print("ouvrage n'exist pas")


    elif x == 14:
        art = input("Donner le nom d'artiste: ")
        c = [p for p in T if isinstance(p,CD) and p.artiste.lower() == art.lower()]
        # if c:
        #     [print(p for p in c)]
        # else:
        #     print("artiste non trouve")

        [print(p) for p in c] if c else print("artiste non trouve")



    elif x == 15:
        aut = input("Donner le nom d'auteur: ")
        c = [p for p in T if isinstance(p,Livre) and p.auteur.lower() == aut.lower()]
        # if c:
        #     [print(p for p in c)]
        # else:
        #     print("auteur non trouve")

        [print(p) for p in c] if c else print("auteur non trouve")


    elif x == 16:
        [print(p) for p in T if isinstance(p,Livre)]
        [print(p) for p in T if isinstance(p,CD)]

    elif x == 17:
        c = sorted(T, key=lambda p: p.nombre_emprunter)
        [print(p) for p in c]

    elif x == 18:
        code = int(input("Donner le code d'ouvrage: "))
        c = search(T,code)
        [print("code n'exist pas") if c is None else c.Emprunter()]

    elif x == 19:
        code = int(input("Donner le code d'ouvrage: "))
        c = search(T,code)

        [print("code n'exist pas") if c is None else c.Restituer()]

    elif x == 20:
        break

    v = input("Do you wish to continue? (Y/N): ")
    if v.lower() != 'y':
        break



















# livre1 = Livre('Titre1','Auteur1','Editeur1')
# print(livre1)
# livre1.Emprunter()
# print(livre1.nombre_emprunter)
# livre1.Restituer()
# livre1.Emprunter()
# print(livre1.nombre_emprunter)



    # if x == 1:
    #     for p in T1:
    #         print(p)
    #     for p in T2:
    #         print(p)
    
    # elif x == 2:
    #     for p in T1:
    #         if p.etat:
    #             print(p)
    #     for p in T2:
    #         if p.etat:
    #             print(p)
    
    # elif x == 3:
    #     for p in T1:
    #         print(p)
    
    # elif x == 4:
    #     for p in T2:
    #         print(p)
    
    # elif x == 5:
    #     for p in T1:
    #         print(p.auteur)
    
    # elif x == 6:
    #     for p in T2:
    #         print(p.artiste)
    
    # elif x == 7:
    #     select = int(input("Ajouter dans les livre ou cd? (1/2): "))
    #     if select == 1:
    #         a1 = input("Donner le titre du livre: ")
    #         a2 = input("Donner l'auteur du livre: ")
    #         a3 = input("Donner l'editeur du livre: ")
    #         T1.append(Livre(a1,a2,a3))
    #     elif select == 2:
    #         a1 = input("Donner le titre du CD: ")
    #         a2 = input("Donner l'artiste du CD: ")
    #         a3 = int(input("Donner le nombre de piste du CD: "))
    #         T2.append(Livre(a1,a2,a3))
    #     else:
    #         raise Exception("Reponse doit etre '1' ou '2' ")

    # elif x == 8:
    #     select = int(input("Supprimer dans les livre ou cd? (1/2): "))
    #     if select == 1:
    #         code = int(input("Donner le code du livre: "))
    #         c = False
    #         for p in T1:
    #             if p.code == code:
    #                 c = True
    #         if c:
    #             for p in T1:
    #                 if p.code == code:
    #                     T1.remove(p)
    #                     break
    #         else:
    #             print("Code n'exist pas")
    #     elif select == 2:
    #         code = int(input("Donner le code du CD: "))
    #         c = False
    #         for p in T2:
    #             if p.code == code:
    #                 c = True
    #         if c:
    #             for p in T2:
    #                 if p.code == code:
    #                     T2.remove(p)
    #                     break
    #     else:
    #         raise Exception("Reponse doit etre '1' ou '2' ")
    
    # elif x == 9:
    #     select = int(input("Modifier le titre dans les livre ou cd? (1/2): "))
    #     if select == 1:
    #         code = int(input("Donner le code du livre: "))
    #         c = False
    #         for p in T1:
    #             if p.code == code:
    #                 c = True
    #         if c:
    #             for p in T1:
    #                 if p.code == code:
    #                     nvtitre = input("Donner le nouveau titre: ")
    #                     p.titre = nvtitre
    #         else:
    #             print("Code n'exist pas")
    #     elif select == 2:
    #         code = int(input("donner le code du CD: "))
    #         c = False
    #         for p in T2:
    #             if p.code == code:
    #                 c = True
    #         if c:
    #             for p in T2:
    #                 if p.code == code:
    #                     nvtitre = input("Donner le nouveau titre: ")
    #                     p.titre = nvtitre
    
    # elif x == 10:
    #     select = int(input("Chercher dans les livre ou les CD? 1/2:  "))
    #     if select == 1:
    #         a = int(input("donner le code de livre: "))
    #         c = [p for p in T1 if p.code == a]
    #         if c:
    #             for p in c:
    #                 print(p)
    #         else:
    #             print("Livre introuvable")
    #     if select == 2:
    #         a = int(input("Donner le code de CD: "))
    #         c = [p for p in T2 if p.code == a]
    #         if c:
    #             for p in c:
    #                 print(p)
    #         else:
    #             print("CD introuvable")
    #     else:
    #         raise ValueError("valeur invalid")
        

    # elif x == 11:
    #     a = int(input("Donner le code de livre: "))
    #     c = [p for p in T1 if p.code == a]
    #     if c:
    #         for p in c:
    #             print(p)
    #     else:
    #         print("Livre intouvable")
    # elif x == 12:

    #     a = int(input("Donner le code de CD: "))
    #     c = [p for p in T2 if p.code == a]
    #     if c:
    #         for p in c:
    #             print(p)
    #     else:
    #         print("CD introuvable")
    
    # elif x == 13:
    #     T3 = T1 + T2
    #     a = input("Donner le titre de l'ouvrage: ")
    #     c = [p for p in T3 if p.titre == a]
    #     if c:
    #         for p in c:
    #             print(p)
    #     else:
    #         print("ouvrage introuvable")

    # elif x == 14:
    #     a = input("Donner le nom d'artiste: ")
    #     c = [p for p in T2 if p.artiste == a]
    #     if c:
    #         for p in c:
    #             print(p)
    #     else:
    #         print("ouvrage introuvable")
        
    # elif x == 15:
    #     a = input("Donner le nom d'auteur: ")
    #     c = [p for p in T1 if p.artiste == a]
    #     if c:
    #         for p in c:
    #             print(p)
    #     else:
    #         print("ouvrage introuvable")
    
    # elif x == 16:
    #     pass

    # elif x == 17:
    #     pass

    # elif x == 18:
    #     select = int(input("Chercher dans les livre ou les CD? 1/2:  "))
    #     if select == 1:
    #         a = int(input("donner le code de livre: "))
    #         c = [p for p in T1 if p.code == a]
    #         if c:
    #             for p in c:
    #                 p.Emprunter()

    #         else:
    #             print("Code livre introuvable")
        
    #     elif select == 2:
    #         a = int(input("Donner le code de CD: "))
    #         c = [p for p in T2 if p.code == a]
    #         if c:
    #             for p in c:
    #                 p.Emprunter()
    #         else:
    #             print("Code CD introuvable")

    
    # elif x == 19:
    #     select = int(input("Chercher dans les livre ou les CD? 1/2: "))
    #     if select == 1:
    #         a = int(input("Donner le code de livre: "))
    #         c = [p for p in T1 if p.code == a]
    #         if c:
    #             for p in c:
    #                 p.Restituer()
        
    #         else:
    #             print("Code livre introuvable")
        
    #     elif select == 2:
    #         a = int(input("Donner le code de CD: "))
    #         c = [p for p in T2 if p.code]
            