class Personne:
    def __init__(self, n="Unknown", a=None, v="unknown"):
        self.nom = n
        self.age = a
        self.ville = v

    def aficher_infos(self):
        print(
            f"Le nom : {self.nom} \n L'age : {self.age} \n Ville : {self.ville} ")


Pers1 = Personne("Said", 20, "Marrakech")
Pers2 = Personne("Mohammed", 26, "Rabat")

Pers1.aficher_infos()
Pers2.aficher_infos()
