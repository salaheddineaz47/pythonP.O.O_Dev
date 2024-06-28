class CompteBancaire:
    def __init__(self, t="Unknown", s=0):
        self.titulaire = t
        self.solde = s

    def afficher_infos(self):
        print(f"Le nom : {self.titulaire}, le solde : {self.solde}")

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if (self.solde >= montant):
            self.solde -= montant


compte1 = CompteBancaire("SALAH", 1000)
compte2 = CompteBancaire("Ahmed", 200)

compte1.afficher_infos()
# compte2.afficher_infos()

# print(compte1.deposer(200))
# print(compte1.retirer(10))
compte1.deposer(200)
compte1.retirer(100)
compte1.afficher_infos()
