class Livre:
    def __init__(self, a="Unknown", t="title unknown"):
        self.auteur = a
        self.titre = t

    def aficher_details(self):
        print(f"l'auteur du Livre titulé {self.titre} est {self.auteur} .")


Livre1 = Livre("Victor Hugo", "Les misérables")
Livre2 = Livre("Ahmed sefrioui", "La boite à Merveilles")
Livre1.auteur = "lllll"
Livre1.aficher_details()
Livre2.aficher_details()
