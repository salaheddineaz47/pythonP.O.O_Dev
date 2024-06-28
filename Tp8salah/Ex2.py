L = {"etudiant_1": 13, "etudiant_2": 17, "etudiant_3": 9,
     "etudiant_4": 15, "etudiant_5": 8, "etudiant_6": 14, "etudiant_7": 16, "etudiant_8": 12}
etudiantAdmis = {}
etudiantNonAdmis = {}


for x in L.keys():
    if L[x] >= 10:
        etudiantAdmis[x] = L[x]
    else:
        etudiantNonAdmis[x] = L[x]

print("-------- Les etudiants admis : ---------")
for x, y in etudiantAdmis.items():
    print(x, y)
print("-------- Les etudiants Non admis : ---------")
for x, y in etudiantNonAdmis.items():
    print(x, y)
