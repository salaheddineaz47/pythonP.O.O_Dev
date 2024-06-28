listeOcc = [1,3,2,1,9,4,1,2,1, 0] 
# print(listeOcc.count(1))
def Parite(L):
    pariteDic = {}
    L.sort()
    for i in range(0, len(L)):
        if(L[i] == 0):
            pariteDic[L[i]] = "Null"
        elif L[i] %2 ==0:
            pariteDic[L[i]] = "pair"
        elif L[i] %2 != 0:
            pariteDic[L[i]] = "impair"
    return pariteDic

listeOcc.sort()
print(listeOcc)

print(Parite(listeOcc))