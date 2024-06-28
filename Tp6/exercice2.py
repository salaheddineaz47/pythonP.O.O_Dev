class Article:
    def __init__(self,nr,n,p,q):
        self.__numero = nr
        self.__nom = n
        self.__prix = p
        self.__quantite = q
    
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self,nr):
        self.__numero = nr
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom = n
    
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,p):
        self.__prix = p
    
    @property
    def quantite(self):
        return self.__quantite
    @quantite.setter
    def quantite(self,q):
        self.__quantite = q
    
    def __str__(self):
        return f"Le numero est {self.__numero}, le nom est {self.__nom}, Le prix a vendre est {self.__prix}, la quantite est {self.__quantite}."

T = [Article(1,'article1',100,50),Article(2,'article2',200,40),Article(3,'article3',300,30),Article(4,'article4',400,20),Article(5,'article5',500,0)]

def search(T,n):
    c = None
    for p in T:
        if p.numero == n:
            c = p
            break
    return c


while True:
    print(f"""
    1.Afficher tous les articles.
          
    2.Afficher les articles en rupture de stock.

    3.Rechercher un article par reference.
    
    4.Rechercher un article par nom.

    5.Rechercher un article par intervalle de prix de vente.

    6.Verifier la disponibilite d'un article.

    7.Ajouter un article au stock.

    8.Supprimer un article par reference.

    9.Modifier un article par reference.

    10.Quitter.
    """)

    x = int(input())

    if x == 1:
        for p in T:
            print(p)
        
    elif x == 2:
        c = [p for p in T if p.quantite == 0]
        if len(c) != 0:
            for p in c:
                print(p)
        else:
            print(f'Aucune quantite est en rupture de stock.')
    
    elif x == 3:
        a = int(input("Donner le numero de reference: "))
        c = search(T,a)
        
        if c != None:
                print(c)
        else:
            print("Code reference introuvable.")
        
    elif x == 4:
        a1 = input("Donner le nom d'article: ")
        c = [p for p in T if p.nom.lower() == a1.lower()]

        if c:
            for p in c:
                print(p)
        else:
            print("Nom introuvable.")
        
    elif x == 5:
        a1 = int(input("Donner le premier nombre: "))
        a2 = int(input("donner le deuxieme nombre: "))
        c = [p for p in T if p.prix > a1 and p.prix < a2]
        if c:
            for p in c:
                print(p)
        else:
            print("Aucune article trouve.")
        
    elif x == 6:
        a = int(input("Donner le code reference d'article: "))
        c = search(T,a)
        if c == None:
            print("Reference introuvable.")
        elif c.quantite != 0:
            print("Disponible.")
        else:
            print("Non disponible.")






        # c = False
        # for p in T:
        #     if p.numero == a:
        #         if p.quantite != 0:
        #             print("L'article est disponible")
        #         else:
        #             print("L'article n'est pas disponible")
        #         c = True
        #         break
        # if not c:
        #     print("Le nom d'article est incorrect")
    
    elif x == 7:
        a1 = int(input("Donner le numero de reference: "))
        c = search(T,a1)
        if c != None:
            print("Numero reference double.")
        else:
            a2 = input("Donner le nom d'article: ")
            a3 = float(input("Donner le prix d'article: "))
            a4 = int(input("Donner sa quantite: "))
            T.append(Article(a1,a2,a3,a4))
            print("Article ajouter.")

    elif x == 8:
        a = int(input("Donner le numero de reference: "))
        c = search(T,a)
        if c == None:
            print("article introuvable")
        else:
            T.remove(c)
            print("Article supprimer")

    elif x == 9:
        a = int(input("Donner le numero de reference: "))
        c = search(T,a)
        
        if c == None:
            print("article introuvable")
        else:
            while True:
                v = int(input("Modifier le nom (1) ou prix (2) ou quantite (3) ou quitter (4): "))
                if v == 1:
                    c.nom = input("Donner le nouveau nom: ")
                    print("article modifier.")
                elif v == 2:
                    c.prix = float(input("Donner le nouveau prix: "))
                    print("article modifier.")
                elif v == 3:
                    c.quantite = int(input("Donner nouveau quantite: "))
                    print("article modifier.")
                elif v == 4:
                    break
                else:
                    print("Choix invalide")

    elif x == 10:
        break        

    v = input("Do you want to continue? Y/N: ")
    if v.lower() != 'y':
        break









