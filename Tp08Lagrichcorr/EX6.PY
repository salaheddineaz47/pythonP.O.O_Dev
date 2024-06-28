print("entrer une chaine de characteres")
c = input()
def longMot(c):
    # listeTexte = []
    listeTexte = c.split()
    dict = {}
    # print(len(listeTexte[1]))
    for x in listeTexte:
        dict[x] = len(x)
        # print(listeTexte[i])
    return dict
print(longMot(c))




