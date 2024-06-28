etudiants={"etudiant 1 " : 13 , "etudiant 2" : 17 , "etudiant 3" : 9 ,
 "etudiant 4" : 15 , "etudiant 5" : 8 , "etudiant 6" : 14 , "etudiant 7" : 16 , "etudiant 8" : 12 }


print(etudiants["etudiant 1 "])

admis = {}
nonAdmis = {}
for et in etudiants:
    if etudiants[et] >=10:
        admis[et] = etudiants[et]
    elif etudiants[et] <10:
        nonAdmis[et] = etudiants[et]

        
print(f"les etudiants admis sont {admis}, \net les et non admis sont {nonAdmis}")