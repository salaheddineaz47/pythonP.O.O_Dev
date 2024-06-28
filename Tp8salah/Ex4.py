def occurence(L):
    d = {}
    for x in L:
        d[x] = L.count(x)
    return d


M = [1, 5, 1, 7, 22, 8, 7, 22]
print(occurence(M))
