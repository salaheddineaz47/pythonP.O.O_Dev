class Etudiant:
    def __init__(self, n="Unknown", m=0, c="Unknown"):
        self.nom = n
        self.matricule = m
        self.cours = c
        self.notes = []

    def afficherdtails(self):
        print(
            f"Le nom est {self.nom}, le matricule : {self.matricule}, cours : {self.cours}")

    def ajouter_note(self, note):
        self.notes.append(note)

    def calcul_moyenne(self):
        s = 0
        for x in self.notes:
            s += x
        return s/len(self.notes)

    def afficher_notes(self):
        print("Note de l'etudiant : ")
        for i in range(len(self.notes)):
            print(f"la note {i+1} : ", self.notes[i])


Etudiant1 = Etudiant("Hamza", 11, 'JAVASCRIPT')
Etudiant2 = Etudiant("MOhamed", 22, "P.O.O")
Etudiant1.afficherdtails()
Etudiant1.ajouter_note(10)
Etudiant1.ajouter_note(18)
Etudiant1.calcul_moyenne()
Etudiant1.afficher_notes()
Etudiant2.afficherdtails()
Etudiant2.ajouter_note(15)
Etudiant2.calcul_moyenne()
Etudiant2.afficher_notes()
Etudiant2.calcul_moyenne()
