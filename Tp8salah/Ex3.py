# L = {"1": 13, "etudiant_2": 17, "etudiant_3": 9,
#      "etudiant_4": 15, "etudiant_5": 8, "etudiant_6": 14, "etudiant_7": 16, "etudiant_8": 12}

n = int(input("Donnez un entier : "))
L = {}

for i in range(1, n+1):
    L[i] = i**2

print(L)
