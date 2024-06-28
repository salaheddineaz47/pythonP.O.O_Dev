listevoitures = [{'num': 1, 'Mat': 'mat1', 'Mar': 'mar1', 'Mod': 'mod1', 'Prix': 300}, {'num': 2, 'Mat': 'mat2', 'Mar': 'mar2', 'Mod': 'mod2', 'Prix': 2}]
# listevoitures = []
numVoitures = len(listevoitures)

def inputVoiture():
        global numVoitures
        numVoitures = numVoitures + 1
        
        voiture ={
        "num" : numVoitures,
        "Mat" : input(f"entrer le matricule de la voiture {numVoitures}:  "),
        "Mar" : input("entrer la marque de la voiture: "),
        "Mod" : input("entrer le modele de la voiture: "),
        "Prix" : int(input("entrer le prix de la voiture: "))
        }
        return voiture 
def enregistrerVoituresnFois(n):
    for i in range (n):
        listevoitures.append(inputVoiture())
def printVoitures(L):
    for i in range(len(L)):
        print(L[i])
def PlusChereVoiture(L):
    prixMax = 0
    voiturePlusChere = []
    for x in listevoitures:
        if x.get("Prix") > prixMax:
            prixMax = x.get("Prix")
    for x in listevoitures:
        if x.get("Prix") == prixMax:
            voiturePlusChere.append(x)

    return voiturePlusChere









# enregistrerVoituresnFois(5)
# printVoitures(listevoitures)
# print(f"La voiture qui a le plus chere prix est {PlusChereVoiture(listevoitures)}")




while True:
    print("\n Menu:\n")
    print("1: enregistrer des voitures")
    print("2: affichier les voitures enregistre. ")
    print("3: affichier la voiture qui le plus chere prix. ")
    x = int(input("Entrez le numéro de votre choix : "))
    if x == 1:
        v = int(input("Entrez le nombre de voitures a entrer: "))
        enregistrerVoituresnFois(v)
    elif x == 2:
        print("la liste des voitures :")
        printVoitures(listevoitures)
    elif x == 3:
        # k= PlusChereVoiture(listevoitures)
        # if len(k) == 0:
        #     print("pas de voitures dans la liste")
        # else:
        #     print(f"La voiture qui a le plus chere prix est {PlusChereVoiture(listevoitures)}")
        listePrix = []
        for x in listevoitures:
            listePrix.append(x.get("Prix"))
        maxPrix = max(listePrix)
        for x in listevoitures:
            if x.get("Prix") == maxPrix:
                print(x)
    else :
        print("choix invalide")
        
    
    u = input("continuer? O/N").lower()
    if u != "o":
        break
