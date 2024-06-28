# Voitures = {"matricule1": 2892, "marque1": "Dacia", "modele1": 2019,
#             "prix1": 20000, "matricule2": 27, "marque2": "Ferrari", "modele2": 2020, "prix2": 9000000}
# Voitures = {}
# for i in range(1, 3):
#     print(f"Donnez les informations de la voiture {i}")
#     m = input(f"Donnez le matricule de la voiture {i} : ")
#     Voitures[f"matricule{i}"] = m
#     marque = input(f"Donnez la marque de la voiture {i} : ")
#     Voitures[f"modele{i}"] = marque
#     md = input(f"Donnez le modèle de la voiture {i} : ")
#     Voitures[f"modele{i}"] = md
#     prix = float(input(f"Donnez le prix de la voiture {i} : "))
#     Voitures[f"prix{i}"] = prix


# maxx = 0
# v = None
# for i in range(1, 3):
#     if Voitures.get(f"prix{i}") > maxx:
#         maxx = Voitures.get(f"prix{i}")
#         v = i


# print(Voitures)
# print(Voitures[f"prix{v}"])

# //////////////////////// AUTRE METHODE ///////////////
# Voitures = [{"matricule": 2892, "marque": "Dacia", "modele": 2019,
#             "prix": 20000}, {"matricule": 27, "marque": "Ferrari", "modele": 2020, "prix": 9000000}, {"matricule": 26, "marque": "Ferr", "modele": 2021, "prix": 9000000}]
Voitures = []

for i in range(1, 3):
    voiture = {}
    print(f"Donnez les informations de la voiture {i}")
    while True:
        m = input(f"Donnez le matricule de la voiture {i} : ")
        k = False
        for d in Voitures:
            if d["matricule"] == m:
                print("matricule deja existant ")
                k = True

        if k is False:
            voiture["matricule"] = m
            break

    ma = input(f"Donnez la marque de la voiture {i} : ")
    voiture["marque"] = ma
    md = input(f"Donnez le modèle de la voiture {i} : ")
    voiture[f"modele"] = md
    prix = float(input(f"Donnez le prix de la voiture {i} : "))
    voiture["prix"] = prix
    Voitures.append(voiture)

for x in Voitures:
    print(x)


k = 0
for x in Voitures:
    if x["prix"] > k:
        k = x["prix"]
for x in Voitures:
    if x["prix"] == k:
        print(x)
