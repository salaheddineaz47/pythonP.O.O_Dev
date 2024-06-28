class InvalideCINException(Exception):
        pass

class stagiaire :
    def __init__(self,CIN,n,p,f,no):
        self.CIN=CIN
        self.__nom=n
        self.__prenom=p
        self.__filiere=f
        self.note=no
    
    @property
    def CIN (self):
        return self.__CIN
    @CIN.setter
    def CIN (self, cin):
        if len(cin) == 5 and cin[0].isalpha()==True and cin[1:].isdigit()==True :
            self.__CIN = cin
        else:
            raise InvalideCINException (f" le CIN est invalide") 
    
        
    @property
    def nom (self):
        return self.__nom
    @nom.setter
    def nom (self,c):
        self.__nom = c
        
        
    @property
    def prenom (self):
        return self.__prenom
    @prenom.setter
    def prenom (self,c):
        self.__prenom = c
    
        
    @property
    def filiere (self):
        return self.__filiere
    @filiere.setter
    def filiere (self,c):
        self.__filiere = c
        
        
    @property
    def note (self):
        return self.__note
    @note.setter
    def note (self,M):
        if isinstance(M, int) and M>= 0 and M<=20 :
            self.__note = M
        else :
            raise Exception ("La Note doit etre entre 0 et 20")
        
        
    def __str__(self) :
        return f"{self.__CIN} - {self.__nom} - {self.__prenom} - {self.__filiere} - {self.__note}"
    

L=[stagiaire("E1234","ahmed","ahmed","DEV",19), stagiaire("E4352","ali","ali","DEV",18), stagiaire("E6754","rami","rami","Reseau",18)]
# L=[]
    
while True :
    
    while True :
        print("*************************************************")
        print("Menu:")
        print("1. Afficher tous les stagiaires.")
        print("2. Afficher les notes de tous les stagiaires.")
        print("3. Afficher les stagiaires ayant une note supérieure ou égale à une note donnée.")
        print("4. Ajouter un stagiaire.")
        print("5. Rechercher un stagiaire par CIN.")
        print("6. Rechercher les stagiaires d'une filière donnée.")
        print("7. Supprimer un stagiaire.")
        print("8. Quitter")

        
        a = input("Entrez le numéro de votre choix : ")
        
        if (a=="1" or a=="2" or a=="3" or a=="4" or a=="5" or a=="6" or a=="7" or a== "8"):
            break
        print("Choix invalide. Veuillez entrer un numéro de 1 à 8.")
        
    
    if (a=="1") :
        if L==[] :
            print("Aucun stagiaire")
        else :
            for s in L:
                print(s)
    
    elif (a=="2"):
        if L==[] :
            print("Aucun stagiare")
        else :
            for s in L:
                print(f"{s.CIN} - {s.note}")
            
    elif (a == "3"):
        
            note_valide=[]
            n = int(input("Entrez la note minimale : "))
            for x in L:
                if x.note >= n:
                    note_valide.append(x)
                    
            if note_valide==[] :
                print("Aucun stagiaire ")
            else:
                for x in note_valide :
                    print(x)
    
    elif a== "4" :
        cin = input("Entrez le CIN : ")
        F = False
        for s in L:
            if s.CIN == cin:
                F = True
                break
        if F :
            print("Erreur : CIN déjà utilisé.")
            
        else :
            n  = input("Entrez le nom : ")
            p = input("Entrez le prénom : ")
            f = input("Entrez la filière : ")
            no= int(input("Entrez la note : "))
            ns = stagiaire(cin, n, p, f , no)
            L.append(ns)
            print("Stagiaire ajouter avec succès.")
            
            
    elif a=="5" :
        r = input("Entrez le CIN à rechercher : ")
                
        satagiaire_recherche1 = None
        # satagiaire_recherche2 = stagiaire("E1111","nom1","prenom1","eee",20)
        T=False
        for x in L:
            if x.CIN == r:
                print(x)
                T=True
                break

        if not T :
            print("Stagiaire non trouvé.")
        
    elif a=="6" :
        filiere_recherche = input("Entrez la filière à rechercher : ")
        meme_filiere = []
        for x in L:
            if x.filiere == filiere_recherche:
                meme_filiere.append(x)
                
        if meme_filiere == [] :
            print("Aucun stagiaire trouvé")
        else :
            for s in meme_filiere:
                print(s)
    
    
    elif a == "7" :
        cin_supprimer = input("Entrez le CIN du stagiaire à supprimer : ")
        
        # L1 = []
        # for x in L:
        #     if x.CIN != cin_supprimer:
        #         L1.append(x)
        # L = L1
        
        T= False
        for x in L :
            if x.CIN == cin_supprimer :
                L.remove(x)
                T = True
                break
        
        if T :
            print("Stagiaire suprimer avec succès.")
        else :
            print ("CIN entrer n'existe pas. ")
        
    elif a == "8":
        print("Programme terminer Merci !!!!!!")
        break
    
    v=input("vous voulez continuer O/N :")
    if (v!="O" and v!="o"):
        break
    
    
    
        
        
        
        
        
        
        
        
        
        
        
    