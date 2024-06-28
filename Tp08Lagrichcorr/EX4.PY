listeOcc = [1,3,2,6,1,4,1,2,1] 
# print(listeOcc.count(1))
def Occurences(L):
    L.sort()
    OccDict = {}
    for x in L:
        OccDict[x] = L.count(x)
    return OccDict
print(Occurences(listeOcc))