def Parite(L):
    d = {}
    for x in L:
        if x == 0:
            d[x] = "Null"
        if x % 2 == 0:
            d[x] = "Paire"
        else:
            d[x] = "Impaire"
    return d


M = [1, 5, 1, 7, 22, 8, 7, 22]
print(Parite(M))
