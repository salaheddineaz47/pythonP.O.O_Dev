class Stagiaire:
    def __init__(self, cne, nom, prenom):
        self.__cne = cne
        self.__nom = nom
        self.__prenom = prenom

    def get_cne(self):
        return self.__cne

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def set_cne(self, cne):
        self.__cne = cne

    def set_nom(self, nom):
        self.__nom = nom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def __str__(self) -> str:
        return f'CNE DE STAGIAIRE: {self.__cne} NOM: {self.__nom} PRENOM: {self.__prenom}\n'

class Groupe:
    # MAX_STAGIAIRES_IN_GROUPE = 25

    def __init__(self, nom_gr, filiere):
        self.__nom_groupe = nom_gr
        self.__filiere = filiere
        # if len(lis) <= Groupe.MAX_STAGIAIRES_IN_GROUPE:
        self.__liste_stagiaires = []
        # else:
        #     raise ValueError(f"The provided list of trainees exceeds the limit ({Groupe.MAX_STAGIAIRES_IN_GROUPE}).")

    @property
    def nom_groupe(self):
        return self.__nom_groupe

    @nom_groupe.setter
    def nom_groupe(self, nom):
        self.__nom_groupe = nom

    @property
    def filiere(self):
        return self.__filiere

    @filiere.setter
    def filiere(self, filiere):
        self.__filiere = filiere

    @property
    def liste_stagiaires(self):
        return self.__liste_stagiaires

    @liste_stagiaires.setter
    def liste_stagiaires(self, lis):
        if len(lis) <= 25:
            self.__liste_stagiaires = lis
        else:
            raise ValueError(f"The provided list of trainees exceeds the limit 25.")

    def add_stagiaire(self, stagiaire):
        if len(self.__liste_stagiaires) < 25 and not self.stagiaire_existe(stagiaire.get_cne()):
            self.__liste_stagiaires.append(stagiaire)
            return True
        else:
             return False

    def __str__(self):
        return f"NOM GROUPE: {self.__nom_groupe} FILIERE: {self.__filiere} LISTE STAGIAIRES:\n {' '.join(str(st) for st in self.__liste_stagiaires)}"

    def rechercher_par_cne(self, cne):
          for stagiaire in self.__liste_stagiaires:
               if stagiaire.get_cne() == cne:
                    return stagiaire
          return None

    def stagiaire_existe(self, cne):
         if self.rechercher_par_cne(cne) == None:
              return False
         else:
              return True

    def stagiaire_existe_nom_prenom(self, nom, prenom):
          return any(stagiaire.get_nom() == nom and stagiaire.get_prenom() == prenom for stagiaire in self.__liste_stagiaires)

    # def ajouter_stagiaire(self, stagiaire):
    #       if len(self.__liste_stagiaires) < Groupe.MAX_STAGIAIRES and not self.stagiaire_existe(stagiaire.cne):
    #            self.__liste_stagiaires.append(stagiaire)
    #            print(f"Stagiaire ajouté au groupe : {stagiaire}")
    #       elif len(self.__liste_stagiaires) >= Groupe.MAX_STAGIAIRES:
    #            print("Impossible d'ajouter le stagiaire. Le groupe est complet.")
    #       else:
    #            print("Impossible d'ajouter le stagiaire. Le CNE existe déjà dans le groupe.")

    def afficher_liste_stagiaires(self):
          print("Liste des stagiaires dans le groupe:")
          for stagiaire in self.__liste_stagiaires:
               print(stagiaire)

    def retirer_stagiaire_par_cne(self, cne):
            if self.stagiaire_existe(cne):
                self.__liste_stagiaires.remove(self.rechercher_par_cne(cne))
                return True
            else:
                 return False


nom = input("enter nom groupe")
fi = input("enter filire groupe")
dev103 = Groupe(nom,fi)
while True:
     try:
          print("menu")
          print("l. recherche un stagiaire par cne.")
          print("2.verifier un stagiaire par nom et prenom.")
          print("3.verifier stagiaire par cne.")
          print("4.Ajouter un stagiaire dont les informations sont entrées par l'utilisateur.")
          print("5.affecher tous les stagiaires.")
          print("6.Supprimer un stagiaire dont le CIN est entré par l'utilisateur.")
          print("7.Quitter")
          d = int(input("choise 1 or 2 or 3 or 4 or 5 or 6 or 7 :"))
     



          if d == 1 :
               s = input("enter le cne ")
               dsa = dev103.rechercher_par_cne(s)
               if dsa == None:
                    print("aucun stagiaire")
               else:
                    print(dsa)





          elif d == 2 :
               nom = input("enter nom ")
               prenom = input("enter prenom ")
               if dev103.stagiaire_existe_nom_prenom(nom,prenom) :
                    print("dispo")
               else:
                    print(" no dispo")



          elif d == 3 :
               cne = input("enter cne ")
               if dev103.stagiaire_existe(cne) :
                    print("dispo")
               else:
                    print(" no dispo")



          elif d == 4 :
                a = input("enter cne stagiare:")
                b = input("enter nom stagiare:")
                c = input("enter prenom stagiare:")
                p = Stagiaire(a,b,c)
                if dev103.add_stagiaire(p):
                     print("added")
                else:
                     print("not added")
              

               


          elif d == 5 :
                dev103.afficher_liste_stagiaires()



          elif d == 6 :

                    c = input("enter cne stagiare:")
                    if dev103.retirer_stagiaire_par_cne(c):
                         print("deleted")
                    else:
                         print(" not deleted")

                    



         
          elif d == 7 :
               p.clear()
               break
          else:
               raise Exception("please enter number in list the choise!!!, idiot!!")
          
     except Exception as m:
          print(m)
